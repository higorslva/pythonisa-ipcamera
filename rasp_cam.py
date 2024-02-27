import cv2
import socket

# Cria um socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta-se ao servidor
sock.connect(("10.42.0.1", 53))

# Captura uma imagem da câmera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Converte a imagem para o formato RGB
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Converte a imagem para bytes
    image_bytes = cv2.imencode(".jpg", image)[1].tostring()

    # Envia a imagem para o servidor
    sock.sendall(image_bytes)

    # Recebe uma resposta do servidor
    response = sock.recv(1024)

    # Mostra a resposta na tela
    print(response)

# Fecha o socket
sock.close()
