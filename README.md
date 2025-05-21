# Sprint-IOT-IA

## TrackYard - Otimizando a Logística com Visão Computacional

### Visão Geral

O **TrackYard** é uma plataforma inovadora que utiliza visão computacional para rastrear e gerenciar motocicletas em tempo real, focada em resolver ineficiências logísticas em operações de grande escala, como as da **Mottu**, que lidam com mais de 100 filiais em diversas plantas no Brasil.

Este projeto combina:

- Backend robusto
- Frontend mobile
- Sistema de leitura de QR Codes

Tudo voltado à **otimização operacional**.

---

### Problema Real

Empresas como a **Mottu** enfrentam desafios críticos na gestão de frotas de motocicletas:

- **Localização Manual**: Gera erros, retrabalho e baixa produtividade.
- **Falta de Visibilidade**: Ausência de dados em tempo real causa atrasos e dificulta a escalabilidade.
- **Riscos e Custos**: A falta de padronização aumenta os riscos de segurança e eleva custos operacionais.

Essas ineficiências prejudicam a expansão de operações logísticas em larga escala, criando a necessidade de uma **solução tecnológica acessível e escalável**.

---

### Justificativa para Visão Computacional

O **TrackYard** adota Visão Computacional como base tecnológica para superar esses desafios:

- 📍 **Rastreamento Preciso**: A leitura de QR Codes elimina processos manuais, reduzindo erros e retrabalho.
- 📈 **Escalabilidade**: Permite rastrear muitas motos em tempo real, independentemente do tamanho da filial.
- 💰 **Custo-Benefício**: Utiliza smartphones e câmeras existentes, evitando hardware caro como GPS.
- ⚙️ **Eficiência Operacional**: Alertas e atualizações em tempo real otimizam a gestão, reduzindo atrasos e custos.

Essa abordagem **minimiza custos de infraestrutura** e **maximiza a acessibilidade**, aproveitando dispositivos já disponíveis.

---

### Tecnologias Utilizadas e Aplicação

#### Backend (Java com Spring Boot)

- **Descrição**: Desenvolvido em Java utilizando o framework Spring Boot.
- **Aplicação**: 
  - Gerencia a lógica de negócios.
  - Processa dados enviados pelo script Python (localização via QR Code).
  - Armazena informações no banco de dados.
  - Fornece APIs RESTful para integração com o frontend.
- **Benefício**: Robusto, escalável e seguro, ideal para grandes volumes de dados em tempo real.

---

#### Frontend Mobile (React Native)

- **Descrição**: Criado com React Native, framework multiplataforma (Android/iOS).
- **Aplicação**: 
  - Interface para escaneamento de QR Codes.
  - Visualização de dados de localização.
  - Recebimento de alertas em tempo real.
  - Geração de relatórios e navegação entre pátios.
- **Benefício**: Experiência fluida e intuitiva em qualquer dispositivo móvel.

---

#### Script Python para Leitura de QR Codes

- **Bibliotecas Utilizadas**: `cv2` (OpenCV), `pyzbar`, `requests`, `time`.

##### Aplicação:

- **Captura de Vídeo**: `cv2.VideoCapture(1)` via DroidCam ou USB.
- **Decodificação**: `pyzbar.decode` identifica QR Codes com `ZBarSymbol.QRCODE`.
- **Processamento**: Tenta ler o conteúdo como JSON e envia via `requests.post` ao backend.
- **Visualização**: Retângulos verdes e texto sobrepostos aos QR Codes com `cv2.rectangle` e `cv2.putText`.
- **Controle de Tempo**: `time.time()` com `read_interval` (3s) evita leituras redundantes.

- **Benefício**: Rastreia em tempo real com baixa latência usando hardware já disponível.

---

### Outras Tecnologias

#### OpenCV (cv2)

- **Aplicação**: Processamento de imagem para validação visual do QR Code.
- **Benefício**: Feedback visual ao operador, melhorando a interface e precisão.

---

### Como Funciona

1. **Escaneamento**: O operador usa o app React Native para capturar imagens via câmera.
2. **Decodificação**: O script Python processa o frame e extrai os dados do QR Code.
3. **Envio ao Backend**: Os dados (em JSON) são enviados ao backend em Spring Boot via POST.
4. **Visualização**: O frontend exibe as informações em tempo real com alertas.
5. **Manutenção**: Atualizações frequentes melhoram desempenho e corrigem erros.

---

### Benefícios

- ✅ Redução de erros com rastreamento automatizado.
- ✅ Visibilidade em tempo real para decisões rápidas.
- ✅ Solução escalável e acessível, ideal para grandes operações logísticas.

---

📷 Leitor de QR Code com Python + Backend Spring Boot
Este projeto implementa um script Python que utiliza Visão Computacional com OpenCV e pyzbar para capturar e decodificar QR Codes, enviando os dados extraídos (em formato JSON) para um backend desenvolvido em Java com Spring Boot.
✅ Requisitos

Python: 3.8 ou superior
Pip: Gerenciador de pacotes do Python
Backend Spring Boot: Rodando localmente em http://localhost:8080/api/movimentacoes
Câmera: Conectada (ex.: DroidCam via USB, webcam ou câmera do notebook)

🛠 Instalação e Execução
1. Clone o repositório (ou crie um diretório para o script)
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

2. (Opcional) Crie um ambiente virtual
python -m venv venv
source venv/bin/activate    # Linux/macOS
venv\Scripts\activate       # Windows

3. Instale as dependências
pip install opencv-python pyzbar requests

⚠️ Atenção (Windows)
No Windows, o pyzbar pode exigir a instalação do ZBar. Use o Chocolatey para instalá-lo:
choco install zbar

🎥 Configuração da Câmera
O script utiliza a seguinte linha para acessar a câmera:
cap = cv2.VideoCapture(1)

O número 1 representa o índice da câmera. Caso esteja usando DroidCam ou múltiplas câmeras, altere para 0, 2, etc., conforme necessário.
▶️ Executando o Script

Certifique-se de que o backend Spring Boot está rodando localmente na porta 8080.
Execute o script:

python qr_reader.py


Aponte a câmera para um QR Code contendo um JSON válido.
Pressione q para sair.

🔄 Como o Script Funciona

Captura de Vídeo: Utiliza OpenCV para capturar vídeo em tempo real.
Decodificação de QR Codes: Usa pyzbar para decodificar QR Codes.
Validação de JSON: Verifica se o conteúdo decodificado é um JSON válido.
Envio ao Backend: Envia os dados ao backend via requests.post.
Feedback Visual: Exibe retângulos verdes e rótulos na tela para indicar a detecção do QR Code.

📦 Exemplo de JSON Esperado no QR Code
{
  "id": "abc123",
  "tipo": "entrada",
  "timestamp": "2025-05-20T15:45:00"
}

💡 Dicas e Soluções
🔍 O script não reconhece a câmera?

Tente alterar o índice da câmera: cv2.VideoCapture(0), cv2.VideoCapture(2), etc.
Verifique se o aplicativo DroidCam está aberto e conectado.

🌐 O backend não responde?

Confirme que o Spring Boot está em execução.
Verifique se a URL http://localhost:8080/api/movimentacoes está acessível.
A URL pode ser ajustada na variável BACKEND_URL no script.

🗂 Estrutura do Projeto
.
├── qr_reader.py         # Script principal
├── README.md            # Instruções de uso
└── requirements.txt     # (Opcional) Dependências





