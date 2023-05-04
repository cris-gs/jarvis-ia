#pip install opencv-python
#pip install deepface==0.0.75

import cv2
import os
from deepface import DeepFace

def capture_and_detect_emotions():
    # Iniciamos la cámara
    cap = cv2.VideoCapture(0)

    # Tomamos la foto y la guardamos temporalmente
    ret, frame = cap.read()
    temp_img = 'temp_img.jpg'
    cv2.imwrite(temp_img, frame)

    # Procesamos la foto para detectar las emociones del rostro
    try:
        result = DeepFace.analyze(temp_img, actions=['emotion'])
        emotions = result['dominant_emotion']
    except:
        os.remove(temp_img)
        return 'Rostro no encontrado'

    # Eliminamos la foto temporal
    os.remove(temp_img)

    if emotions == 'happy':
        emotions = 'Feliz'
    elif emotions == 'angry':
        emotions = 'Enojado'
    elif emotions == 'neutral':
        emotions = 'Neutral'
    elif emotions == 'sad':
        emotions = 'Triste'
    elif emotions == 'surprise':
        emotions = 'Sorprendido'
    else:
        emotions = 'Desconocido'

    return emotions

# print(capture_and_detect_emotions())