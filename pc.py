import cv2
import numpy as np
import socket
import time

# Configurações do servidor UDP
host = '0.0.0.0'  # Escuta em todos os endereços disponíveis
port = 12345  # Porta UDP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

# Variáveis para calcular FPS
fps_start_time = time.time()
fps_frame_count = 0

while True:
    data, addr = sock.recvfrom(65535)  # Recebe os dados do endereço da Raspberry Pi

    if len(data) > 0:
        frame = np.frombuffer(data, dtype=np.uint8)  # Converte os dados recebidos de volta para o frame
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)  # Decodifica o frame JPEG

        if frame is not None and frame.shape[0] > 0 and frame.shape[1] > 0:
            # Calcula FPS
            fps_frame_count += 1
            elapsed_time = time.time() - fps_start_time
            if elapsed_time > 1:  # Atualiza FPS a cada segundo
                fps = fps_frame_count / elapsed_time
                fps_text = f"FPS: {fps:.2f}"
                fps_frame_count = 0
                fps_start_time = time.time()

            # Desenha o texto de FPS na imagem
            cv2.putText(frame, fps_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow('Received', frame)  # Mostra o frame recebido

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Pressione 'q' para sair
        break

cv2.destroyAllWindows()  # Fecha todas as janelas abertas

