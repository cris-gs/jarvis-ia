import os
import pytube
import cv2
from Mask_RCNN.samples.coco import coco
from Mask_RCNN.mrcnn import model as modellib
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)

#* pip install pytube
#* pip install scikit-image

#TODO: instalar en visual studio installer el paquete llamado 'Desktop development with C++ y marcar las casillas de la izquierda(https://i.stack.imgur.com/DKWVM.png)'

#?Abre una terminal o línea de comandos y ejecuta el siguiente comando para clonar el repositorio de Mask_RCNN:
#! OJO: NO ES NECESARIO SI YA EXISTE LA CARPETA Mask_RCNN CON SUS ARCHIVOS
#* git clone --quiet https://github.com/ParthGaneriwala/Mask_RCNN
#? Ve al directorio del repositorio clonado:
#* cd Mask_RCNN
#? Instala las dependencias requeridas ejecutando el siguiente comando:
#* pip install -r requirements.txt
#? Vuelve a la ruta inicial
#* cd ..

#* pip install pycocotools
#* pip install mrcnn
#* pip install keras

def video_scan(url):
  # Root directory of the project
  ROOT_DIR = os.path.abspath("./root")
  # Directory to save logs and trained model
  MODEL_DIR = os.path.join(ROOT_DIR, "logs")

  class InferenceConfig(coco.CocoConfig):
      # Set batch size to 1 since we'll be running inference on
      # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
      PRE_NMS_LIMIT = 6000  # Ejemplo: asigna un valor específico
      GPU_COUNT = 1
      IMAGES_PER_GPU = 1

  config = InferenceConfig()
  config.display()

  # Descargar el video de YouTube
  # video_url = 'https://www.youtube.com/shorts/LdDtPuY89T8'
  youtube = pytube.YouTube(url)
  video = youtube.streams.get_highest_resolution()
  video_path = video.download('./videos')
  bothKnives = [False, False]
  responses = []

  # Crear una nueva instancia del modelo
  model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

  # Cargar los pesos del modelo desde el archivo
  model.keras_model.load_weights('./Modelos/pesos_modelo_armas.h5')

  class_names = ['BG', 'person', 'bicycle', 'car', 'motorcycle', 'airplane',
                'bus', 'train', 'truck', 'boat', 'traffic light',
                'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird',
                'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear',
                'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie',
                'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
                'kite', 'baseball bat', 'baseball glove', 'skateboard',
                'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup',
                'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
                'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
                'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed',
                'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote',
                'keyboard', 'cell phone', 'microwave', 'oven', 'toaster',
                'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors',
                'teddy bear', 'hair drier', 'toothbrush']

  # Leer el video y analizar los frames
  cap = cv2.VideoCapture(video_path)
  frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

  for i in range(frame_count):
      # Leer el siguiente frame
      ret, frame = cap.read()

      # Realizar la detección de objetos en el frame
      results = model.detect([frame], verbose=1)
      r = results[0]

      # Imprimir el nombre de los objetos detectados
      for class_id in r['class_ids']:
          class_name = class_names[class_id]
          if class_name == 'scissors': 
            print("SE ENCONTRÓ UNA TIJERA")
            bothKnives[0] = True
            if not ('Se han encontrado tijeras en el video' in responses):
              responses.append('Se han encontrado tijeras en el video')
          if class_name == 'knife': 
            print("SE ENCONTRÓ UN CUCHILLO")
            bothKnives[1] = True
            if not ('Se han encontrado cuchillos en el video' in responses):
              responses.append('Se han encontrado cuchillos en el video')
      if all(bothKnives):        
        return responses

  # Liberar recursos
  cap.release()
  return responses
