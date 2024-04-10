import cv2
import numpy as np
import socket
import time
import logging

COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

class_names = []
with open("plates.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

# Configurações do servidor UDP
host = '0.0.0.0'  # Escuta em todos os endereços disponíveis
port = 12345  # Porta UDP
buffer_size = 65507  # Tamanho máximo de um pacote UDP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

net = cv2.dnn.readNet("plates-yolov4-tiny-detector.weights", "plates-yolov4-tiny-detector.cfg")

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)

while True:
    data, _ = sock.recvfrom(65535)  # Recebe os dados do endereço da Raspberry Pi
    frame = np.frombuffer(data, dtype=np.uint8)  # Converte os dados recebidos de volta para o frame
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)  # Decodifica o frame JPEG

    if frame is None or frame.size == 0:
        logging.error("Frame vazio ou inválido.")
        continue

    # Redimensionar o frame para as dimensões corretas
    frame = cv2.resize(frame, (416, 416))

    start = time.time()

    classes, scores, boxes = model.detect(frame, confThreshold=0.1, nmsThreshold=0.2)

    end = time.time()

    for (classid, score, box) in zip(classes, scores, boxes):
        class_id = classid[0] if isinstance(classid, np.ndarray) else classid
        score_val = score[0] if isinstance(score, np.ndarray) else score
        label = f'{class_names[int(class_id)]} : {round(float(score_val), 2)}'
        color = COLORS[int(class_id) % len(COLORS)]
        cv2.rectangle(frame, box, color, 2)
        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    fps_label = f'FPS: {round((1.0 / (end - start)), 2)}'
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("detections", frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
