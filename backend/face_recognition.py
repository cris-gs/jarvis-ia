import cv2
import os
from deepface import DeepFace

# Ruta donde se guardarán las imágenes
image_path = "C:/Users/Personal/Desktop/TEC/Semestre 7/Inteligencia Artificial/Proyecto 2/images/derian"

def capture_and_detect_emotions():
    # Iniciamos la cámara
    cap = cv2.VideoCapture(0)

    print(os.getcwd())

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

    if os.path.exists(temp_img):
        # Generar el nombre de archivo de imagen basado en la cantidad de archivos en la carpeta
        files = os.listdir(image_path)
        number_files = len(files)
        image_name = "image" + str(number_files + 1) + ".jpg"

        # Mover la imagen temporal a la ruta de destino con el nombre generado
        image_destiny = os.path.join(image_path, image_name)
        os.rename(temp_img, image_destiny)

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
