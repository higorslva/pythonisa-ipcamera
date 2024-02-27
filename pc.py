import cv2
import numpy as np
import socket

# Configurações do servidor UDP
host = '0.0.0.0'  # Escuta em todos os endereços disponíveis
port = 12345  # Porta UDP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

while True:
    data, addr = sock.recvfrom(65535)  # Recebe os dados do endereço da Raspberry Pi
    frame = np.frombuffer(data, dtype=np.uint8)  # Converte os dados recebidos de volta para o frame
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)  # Decodifica o frame JPEG

    cv2.imshow('Received', frame)  # Mostra o frame recebido

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
        break

cv2.destroyAllWindows()  # Fecha todas as janelas abertas
