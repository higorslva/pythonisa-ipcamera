# Pythonisa - Câmeras IP

Este repositório contém o código fonte utilizado no projeto Pythonisa para conexão de uma Raspberry PI com módulo de câmera em um servidor central. O Pythonisa é um projeto vinculado ao CNPq para monitoramento de ônibus em Macapá.

## Funcionalidades

- **Conexão de Câmeras IP**: O código incluído neste repositório permite estabelecer conexões com uma Raspberry PI com módulo de câmera.

## Pré-requisitos
#### Raspberry:
- Python 3.x
- Biblioteca [OpenCV](https://pypi.org/project/opencv-python/)
- Biblioteca [Numpy](https://numpy.org/)
- Raspberry Pi com módulo de câmera
- Raspberry Pi OS (Legacy Bullseye)

### PC:
 - Python 3.x
 - Biblioteca [OpenCV](https://pypi.org/project/opencv-python/)
 - Biblioteca [Numpy](https://numpy.org/)

## Como Usar

1. Clone este repositório em seu ambiente de desenvolvimento local (No seu PC):

   ```
   git clone https://github.com/higorslva/pythonisa-ipcamera.git
   ```

2. Instale as dependências necessárias executando o seguinte comando:

   ```
   pip install -r requirements.txt
   ```

3. Garanta que ambos estejam na mesma rede local. Altere o endereço IP no arquivo ```rasp.py```
*PS: Apenas o arquivo ```rasp.py``` precisa estar na sua Raspberry. Você pode conectar com SSH e copiar e colar o código para lá.*

4. Execute o código na Raspberry:

   ```
   python rasp.py
   ```
5. Execute o código no PC:

   ```
   python main_camera.py
   ```

## Licença

Este projeto está licenciado sob a licença GNU v3.0. Consulte o arquivo `LICENSE` para obter mais informações.
