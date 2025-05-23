import json
import qrcode
from datetime import datetime

# Dados a serem enviados
data = {
    "idMovimentacao": 2,
    "idMoto": "MOTO001",
    "idPonto": 2,
    "dataHora": datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
}

# Gera o JSON
json_data = json.dumps(data)
print("JSON Gerado:\n", json_data)

# Gera o QR Code com o JSON
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(json_data)
qr.make(fit=True)

# Cria a imagem do QR Code
img = qr.make_image(fill='black', back_color='white')
img.save("qrcode4.png")

print("QR Code salvo como qrcode.png")