import cv2
import json
import requests
import time
from pyzbar.pyzbar import decode, ZBarSymbol

# URL do backend Java
BACKEND_URL = "http://localhost:8080/api/movimentacoes"

def send_post_request(json_data):
    try:
        response = requests.post(BACKEND_URL, json=json_data)
        print(f"Resposta do backend: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Erro ao enviar POST: {e}")

def main():
    # Inicializa a captura de vídeo com o índice do DroidCam via USB
    cap = cv2.VideoCapture(0)  # Substitua para "1" caso use o droidcam
    print("Aponte a câmera do celular para um QR Code")

    last_read_time = 0
    read_interval = 3  # Intervalo de 3 segundos

    while True:
        # Captura frame por frame
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar vídeo. Verifique a conexão com o DroidCam.")
            break

        current_time = time.time()

        # Verifica se o intervalo de leitura foi atingido
        if current_time - last_read_time >= read_interval:
            try:
                # Decodifica o QR Code no frame
                qr_codes = decode(frame, symbols=[ZBarSymbol.QRCODE])
            except Exception as e:
                print(f"Erro na decodificação: {e}")
                qr_codes = []

            for qr_code in qr_codes:
                try:
                    qr_data = qr_code.data.decode('utf-8')
                    print(f"QR Code detectado: {qr_data}")

                    # Tenta carregar o QR Code como JSON
                    try:
                        json_data = json.loads(qr_data)
                        print("JSON válido detectado")
                        send_post_request(json_data)
                    except json.JSONDecodeError:
                        print("QR Code não contém um JSON válido")

                    # Desenha um retângulo em volta do QR Code
                    (x, y, w, h) = qr_code.rect
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, "JSON Detectado" if 'json_data' in locals() else "QR Code", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                except Exception as e:
                    print(f"Erro ao processar QR Code: {e}")

            # Atualiza o último tempo de leitura
            last_read_time = current_time

        # Exibe o frame
        cv2.imshow('QR Code Reader', frame)

        # Pressione 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Libera a câmera e fecha as janelas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
