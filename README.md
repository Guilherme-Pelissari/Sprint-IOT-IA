TrackYard - Otimizando a Logística com Visão Computacional
Visão Geral
O TrackYard é uma plataforma inovadora que utiliza visão computacional para rastrear e gerenciar motocicletas em tempo real, focada em resolver ineficiências logísticas em operações de grande escala, como as da Mottu, que lidam com mais de 100 filiais em diversas plantas no Brasil. Este projeto combina backend robusto, frontend mobile e um sistema de leitura de QR Codes para otimização operacional.
Problema Real
Empresas de logística, como a Mottu, enfrentam desafios críticos na gestão de frotas de motocicletas:

Localização Manual: O rastreamento manual gera erros, retrabalho e baixa produtividade.
Falta de Visibilidade: Ausência de dados em tempo real causa atrasos e dificuldades de escalabilidade.
Riscos e Custos: A falta de padronização aumenta riscos de segurança e eleva custos operacionais, impactando a eficiência e a experiência do cliente.

Essas ineficiências prejudicam a expansão de operações logísticas em larga escala, criando a necessidade de uma solução tecnológica acessível e escalável.
Justificativa para Visão Computacional
O TrackYard adota Visão Computacional como base tecnológica para superar esses desafios:

Rastreamento Preciso: A leitura de QR Codes elimina processos manuais, reduzindo erros e retrabalho.
Escalabilidade: Permite rastrear milhares de motos em tempo real, independentemente do tamanho da filial.
Custo-Benefício: Ao contrário de soluções IoT (como GPS), que exigem hardware caro e manutenção constante, a visão computacional utiliza smartphones e câmeras existentes, oferecendo uma solução econômica e sustentável.
Eficiência Operacional: Alertas e atualizações em tempo real otimizam a gestão, reduzindo atrasos e custos.

A escolha pela visão computacional em vez de IoT tradicional reflete a necessidade de minimizar custos de infraestrutura e maximizar a acessibilidade para operadores, aproveitando dispositivos já disponíveis.
Tecnologias Utilizadas e Aplicação
Backend (Java com Spring Boot)

Descrição: O backend é desenvolvido em Java utilizando o framework Spring Boot, hospedado em http://localhost:8080/api/movimentacoes.
Aplicação: Gerencia a lógica de negócios, processa dados enviados pelo script Python (ex.: localização de motos via QR Codes), armazena informações no banco de dados e fornece APIs RESTful para integração com o frontend. Recebe requisições POST com dados JSON e retorna respostas de status.
Benefício: Garante robustez, escalabilidade e segurança para lidar com grandes volumes de dados em tempo real.

Frontend Mobile (React Native)

Descrição: O frontend mobile é construído com React Native, uma framework que permite criar aplicativos multiplataforma (Android/iOS).
Aplicação: Oferece uma interface intuitiva para operadores escanearem QR Codes, visualizar dados de localização e receber alertas em tempo real. Integra-se ao backend via APIs para exibir informações atualizadas e suporta funcionalidades como navegação entre pátios e geração de relatórios.
Benefício: Proporciona uma experiência consistente e rápida, aproveitando a portabilidade para diferentes dispositivos móveis.

Script Python para Leitura de QR Codes

Descrição: Um script Python utiliza bibliotecas como cv2 (OpenCV), pyzbar, requests e time para capturar e decodificar QR Codes via câmera.
Aplicação:
Captura de Vídeo: Usa cv2.VideoCapture(1) para acessar a câmera (via DroidCam ou USB), capturando frames continuamente.
Decodificação: A biblioteca pyzbar.decode identifica e decodifica QR Codes no frame, usando ZBarSymbol.QRCODE para especificidade.
Processamento: Tenta interpretar o conteúdo do QR Code como JSON com json.loads. Se válido, envia os dados ao backend via requests.post para BACKEND_URL.
Visualização: Desenha retângulos verdes em torno dos QR Codes detectados com cv2.rectangle e exibe texto com cv2.putText, além de mostrar o feed ao vivo com cv2.imshow.
Controle de Tempo: O time.time() e read_interval (3 segundos) evitam leituras redundantes, otimizando o desempenho.


Benefício: Permite rastreamento em tempo real com baixa latência, utilizando hardware existente (smartphones) e integrando-se ao backend para atualizações instantâneas.

Outras Tecnologias

OpenCV (cv2):
Aplicação: Processa imagens capturadas para desenhar retângulos e texto no frame, facilitando a validação visual do QR Code.
Benefício: Melhora a interface do operador com feedback visual em tempo real.


Firebase (Opcional):
Aplicação: Pode ser usado para autenticação, notificações push e armazenamento complementar, integrando-se ao backend.
Benefício: Suporta escalabilidade e notificações automáticas.



Como Funciona

Escaneamento: O operador usa o app React Native para capturar frames via câmera (conectada por DroidCam).
Decodificação: O script Python processa o frame, decodifica o QR Code e extrai os dados.
Envio ao Backend: Dados válidos (JSON) são enviados ao Spring Boot via POST, atualizando o sistema.
Visualização: O frontend exibe os dados em tempo real, com alertas automáticos.
Manutenção: Atualizações periódicas corrigem bugs e otimizam o desempenho.

Benefícios

Redução de erros com rastreamento automatizado.
Visibilidade em tempo real para decisões ágeis.
Solução escalável e acessível, ideal para logística em grande escala.

Próximos Passos

Testes pilotos em 5 filiais da Mottu.
Integração com APIs de sistemas ERP (ex.: SAP).
Expansão para outras empresas de logística automotiva.


TrackYard – Otimizando a Logística, Um Rastro de Cada Vez!
# Sprint-IOT-IA
