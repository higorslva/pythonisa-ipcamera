# Pythonisa - Câmeras IP

Este repositório contém o código fonte utilizado no projeto Pythonisa para conexão de câmeras IP em um servidor central. O Pythonisa é um projeto vinculado ao CNPq para monitoramento de ônibus em Macapá.

## Funcionalidades

- **Conexão de Câmeras IP**: O código incluído neste repositório permite estabelecer conexões com câmeras IP compatíveis, permitindo o acesso remoto às suas transmissões de vídeo (incluindo Raspberry Pi com módulo PiCamera).

## Pré-requisitos

- Python 3.x
- Biblioteca [OpenCV](https://pypi.org/project/opencv-python/)

## Como Usar

1. Clone este repositório em seu ambiente de desenvolvimento local:

   ```
   git clone https://github.com/higorslva/pythonisa-ipcamera.git
   ```

2. Instale as dependências necessárias executando o seguinte comando:

   ```
   pip install -r requirements.txt
   ```

3. Configure as câmeras IP que deseja conectar ao servidor central, garantindo que os endereços IP, portas e credenciais estejam corretos.

4. Execute o código na raspberry:

   ```
   python rasp.py
   ```
5. Execute o código no PC:

   ```
   python pc.py
   ```   

## Licença

Este projeto está licenciado sob a licença GNU v3.0. Consulte o arquivo `LICENSE` para obter mais informações.
