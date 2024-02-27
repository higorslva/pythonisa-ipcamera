import cv2
import numpy as np
import socket

# Configurações do servidor UDP
host = '10.42.0.1'  # Insira o IP do seu computador aqui
port = 12345  # Porta UDP
buffer_size = 65507  # Tamanho máximo de um pacote UDP

cap = cv2.VideoCapture(0)  # Inicia a captura de vídeo da câmera (0 para a câmera padrão)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    ret, frame = cap.read()  # Captura um frame da câmera
    encoded_frame = cv2.imencode('.jpg', frame)[1]  # Codifica o frame para JPEG
    data = np.array(encoded_frame).tobytes()  # Converte o frame em bytes

    # Envia os dados via UDP para o computador dividindo em pacotes menores
    for i in range(0, len(data), buffer_size):
        sock.sendto(data[i:i+buffer_size], (host, port))

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
        break

cap.release()  # Libera a captura de vídeo
cv2.destroyAllWindows()  # Fecha todas as janelas abertas
