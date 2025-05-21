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

# 📷 Leitor de QR Code com Envio para Backend Java

Este script utiliza a webcam (incluindo a do celular via DroidCam) para detectar QR Codes em tempo real, interpretar os dados como JSON e enviá-los para uma API REST em um backend Java.

---

## 🚀 Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes do Python)
- Backend Java rodando em `http://localhost:8080/api/movimentacoes`
- (Opcional) DroidCam instalado e funcionando se for usar a câmera do celular

---

## 🧰 Instalação

### 1. Clone o repositório ou salve o script:

```bash
git clone https://github.com/seuusuario/seurepositorio.git
cd seurepositorio
``` 

## 2. (Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
``` 
## 3. Instale as dependências

```bash
pip install opencv-python pyzbar requests
```

> ⚠️ **Windows:** pode ser necessário instalar o ZBar manualmente:
>
> **Via Chocolatey:**
>
> ```bash
> choco install zbar
> ```
>
> Ou baixe o instalador manualmente:  
> [https://github.com/NaturalHistoryMuseum/pyzbar#windows](https://github.com/NaturalHistoryMuseum/pyzbar#windows)

---

## ⚙️ Configuração

- Verifique o índice da câmera no trecho `cv2.VideoCapture(0)`.  
  Pode ser necessário trocar `1` por `0`, `2`, etc. geralmente o `0`se for utilizar a webcam nativa e o `1`se conectar o smartphone via droidcam para usar a camera do celular

---

## ▶️ Como executar

```bash
python nome_do_script.py
```
> Substitua `nome_do_script.py` pelo nome do arquivo salvo com o código.

---

## 🧪 Funcionamento

- A câmera será ativada e começará a escanear QR Codes.
- Ao encontrar um QR Code com **JSON válido**, o conteúdo será enviado via **POST** para o backend.
- Há um intervalo de **3 segundos** entre cada leitura.
- Pressione `q` para encerrar o programa.

---





