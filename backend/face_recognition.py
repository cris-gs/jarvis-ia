import cv2
import os
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

# Ver los paquetes instalados
# pip list

# Desinstalar 
# pip uninstall tensorflow tensorflow-hub tensorflow-estimator tensorflow-io-gcs-filesystem absl-py astunparse gast google-auth google-auth-oauthlib google-pasta grpcio h5py keras-preprocessing numpy opt-einsum protobuf tensorboard tensorboard-data-server tensorboard-plugin-wit tensorflow-intel tensorflow-io-gcs-filesystem termcolor tf-estimator-nightly typing-extensions wrapt

# Instalar
# pip install tensorflow tensorflow-hub

def KerasLayerModule(handle, trainable=False, dtype=tf.float32, name=None, **kwargs):
    return hub.KerasLayer(handle, trainable=trainable, dtype=dtype, name=name, **kwargs)

model = tf.keras.models.load_model('./Modelos/reconocimientoFacial.h5', custom_objects={'KerasLayer': KerasLayerModule})

# print(os.getcwd())

# Ruta donde se guardarán las imágenes
# image_path = "C:/Users/Personal/Desktop/TEC/Semestre 7/Inteligencia Artificial/Proyecto 2/images/derian"

def preprocess_image(image):
    # Cambiar el tamaño de la imagen a (224, 224)
    resized_image = cv2.resize(image, (224, 224))

    # Convertir la imagen a un array numpy y normalizar los valores de píxeles
    normalized_image = resized_image.astype(np.float32) / 255.0

    # Expandir las dimensiones del array para que coincida con el formato de entrada del modelo
    preprocessed_image = np.expand_dims(normalized_image, axis=0)

    return preprocessed_image

def facial_recognition():
    # Iniciamos la cámara
    cap = cv2.VideoCapture(0)

    # Tomamos la foto y la guardamos temporalmente
    ret, frame = cap.read()
    temp_img = 'temp_img.jpg'
    cv2.imwrite(temp_img, frame)

    # Procesamos la foto para detectar el rostro
    if model is not None:
        if os.path.exists(temp_img):
            # Cargamos la imagen temporal
            img = cv2.imread(temp_img)

            # Preprocesamos la imagen
            preprocessed_img = preprocess_image(img)

            # Realizamos la predicción
            prediccion = model.predict(preprocessed_img)
            clase_predicha = np.argmax(prediccion)

            if clase_predicha == 0:
                message = "Hola Cristopher, ¡qué bueno verte de nuevo!"
            elif clase_predicha == 1:
                message = "Hola Derian, ¡qué bueno verte de nuevo!"
            else:
                message = "Lo siento, pero no reconozco tu rostro."

            # Generar el nombre de archivo de imagen basado en la cantidad de archivos en la carpeta
            # files = os.listdir(image_path)
            # number_files = len(files)
            # image_name = "image" + str(number_files + 1) + ".jpg"

            # # Mover la imagen temporal a la ruta de destino con el nombre generado
            # image_destiny = os.path.join(image_path, image_name)
            # os.rename(temp_img, image_destiny)

            return message 

    else:
        os.remove(temp_img)
        return 'Modelo de reconocimiento facial no encontrado'

    os.remove(temp_img)
    return "Rostro no reconocido"

#facial_recognition()