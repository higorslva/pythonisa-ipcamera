import cv2
import numpy as np
import socket
import time

COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]

class_names = []
with open("coco.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

# Configurações do servidor UDP
host = '0.0.0.0'  # Escuta em todos os endereços disponíveis
port = 12345  # Porta UDP
buffer_size = 65507  # Tamanho máximo de um pacote UDP

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((host, port))

net = cv2.dnn.readNet("yolov4-tiny.weights", "yolov4-tiny.cfg")

model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416, 416), scale=1/255)

while True:

    data, _ = sock.recvfrom(65535)  # Recebe os dados do endereço da Raspberry Pi
    frame = np.frombuffer(data, dtype=np.uint8)  # Converte os dados recebidos de volta para o frame
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)  # Decodifica o frame JPEG

    start = time.time()

    classes, scores, boxes = model.detect(frame, 0.1, 0.2)

    end = time.time()

    for (classid, score, box) in zip(classes, scores, boxes):

        color = COLORS[int(classid) % len(COLORS)]

        label = f'{class_names[classid]} : {score*100:.2f}%'

        cv2.rectangle(frame, box, color, 2)

        cv2.putText(frame, label, (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    fps_label = f'FPS: {round((1.0 / (end - start)), 2)}'

    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 5)
    cv2.putText(frame, fps_label, (0, 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("detections", frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
