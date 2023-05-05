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
        emotions = 'Usted se encuentra feliz 😀'
    elif emotions == 'angry':
        emotions = 'Usted se encuentra enojado 😠'
    elif emotions == 'neutral':
        emotions = 'Usted se encuentra neutral 😐'
    elif emotions == 'sad':
        emotions = 'Usted se encuentra triste 😢'
    elif emotions == 'surprise':
        emotions = 'Usted se encuentra sorprendido 😮'
    else:
        emotions = 'Sentimiento desconocido 🤨'

    return emotions

# print(capture_and_detect_emotions())