import cv2
import numpy as np
import socket
import logging

# Configurações de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Configurações do servidor UDP
host = '192.168.1.67'  # Insira o IP do seu computador aqui
port = 12345  # Porta UDP

min_buffer_size = 1400  # Tamanho mínimo do buffer
max_buffer_size = 65507  # Tamanho máximo do buffer
buffer_size = min_buffer_size  # Tamanho inicial do buffer

cap = cv2.VideoCapture(0)  # Inicia a captura de vídeo da câmera (0 para a câmera padrão)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    ret, frame = cap.read()  # Captura um frame da câmera
    encoded_frame = cv2.imencode('.jpg', frame)[1]  # Codifica o frame para JPEG
    data = np.array(encoded_frame).tobytes()  # Converte o frame em bytes

    # Envia os dados via UDP para o computador dividindo em pacotes menores
    num_packets = 0
    for i in range(0, len(data), buffer_size):
        packet = data[i:i+buffer_size]
        try:
            sock.sendto(packet, (host, port))
            num_packets += 1
            logging.info(f"Enviado pacote {num_packets} de tamanho {len(packet)} bytes")
        except Exception as e:
            logging.error(f"Erro ao enviar pacote {num_packets}: {str(e)}")
            break

    # Verifica se houve perdas
    # Se sim, diminui o tamanho do buffer
    # Se não, aumenta o tamanho do buffer se estiver abaixo do máximo
    houve_perdas = False  # Suponha que não houve perdas
    # Código simulado para verificar se houve perdas
    # Aqui você deve inserir a lógica real para verificar perdas
    # Por exemplo, contar os ACKs recebidos ou um método similar
    # Suponha que houve perdas aleatoriamente para fins de exemplo
    if np.random.rand() < 0.1:  # 10% de chance de haver perdas
        houve_perdas = True

    if houve_perdas:
        buffer_size = max(min_buffer_size, buffer_size // 2)
        logging.info(f"Tamanho do buffer ajustado para {buffer_size} bytes devido a perda de pacotes.")
    else:
        if buffer_size < max_buffer_size:
            buffer_size = min(max_buffer_size, buffer_size * 2)
            logging.info(f"Tamanho do buffer ajustado para {buffer_size} bytes.")

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
        break

cap.release()  # Libera a captura de vídeo
cv2.destroyAllWindows()  # Fecha todas as janelas abertas
