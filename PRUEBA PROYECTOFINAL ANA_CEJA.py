#pip install opencv-python ultralytics
#pip install opencv-python pandas numpy ultralytics
#pip install ultralytics

import cv2
import numpy as np
import pandas as pd
from ultralytics import YOLO
import time

# Cargar el modelo YOLOv8
model = YOLO("yolov8n.pt")

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Lista para almacenar detecciones
detections_list = []

# Diccionario para traducir etiquetas
etiquetas_espanol = {
    "person": "persona",
    "dog": "perro",
    "bicycle": "bicicleta",
    "cell phone":"telefono celular",
    "vase": "florero",
    "sports ball": "pelota deportiva",
    "car": "auto",
    "chair": "silla",
    "desk": "escritorio",
    "table": "mesa",
    "board": "pizarrón",
    "blackboard": "pizarrón negro",
    "whiteboard": "pizarrón blanco",
    "marker": "marcador",
    "pen": "pluma",
    "pencil": "lápiz",
    "eraser": "borrador",
    "notebook": "cuaderno",
    "book": "libro",
    "backpack": "mochila",
    "laptop": "laptop",
    "computer": "computadora",
    "mouse": "ratón",
    "keyboard": "teclado",
    "projector": "proyector",
    "screen": "pantalla",
    "clock": "reloj",
    "ruler": "regla",
    "calculator": "calculadora",
    "scissors": "tijeras",
    "stapler": "engrapadora",
    "paper": "hoja de papel",
    "folder": "carpeta",
    "glue": "pegamento",
    "highlighter": "resaltador",
    "speaker": "bocina",
    "microphone": "micrófono",
    "fan": "ventilador",
    "trash bin": "bote de basura",
    "door": "puerta",
    "window": "ventana",
    "curtain": "cortina",
    "lamp": "lámpara",
    "air conditioner": "aire acondicionado",
    "heater": "calefactor",
    "student": "estudiante",
    "teacher": "maestro",
    "schoolbag": "bolsa escolar"
}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detectar objetos en la imagen
    results = model(frame)

    # Procesar los resultados y almacenarlos en pandas
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]
            label_es = etiquetas_espanol.get(label, label)

            # Guardar en lista para DataFrame
            detections_list.append([label_es, conf, x1, y1, x2, y2, time.time()])

            # Dibujar el cuadro y la etiqueta en la imagen
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label_es}: {conf:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Mostrar la imagen con detecciones
    cv2.imshow("Detección de Objetos", frame)

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Convertir a DataFrame de pandas
df = pd.DataFrame(detections_list, columns=["Objeto", "Confianza", "X1", "Y1", "X2", "Y2", "Tiempo"])

# Guardar a CSV
df.to_csv("detecciones.csv", index=False)

# Mostrar estadística básica
print("\nResumen de detecciones:")
print(df.groupby("Objeto").agg({"Confianza": ["count", "mean"]}))

# Liberar recursos
cap.release()
cv2.destroyAllWindows()

