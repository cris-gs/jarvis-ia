# from voice import *
from voice_recognition import *
from face_recognition import capture_and_detect_emotions
from options import menu
import pyttsx3

# Definimos el punto de entrada de nuestro programa
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def init():
    if request.path == '/':
        return 'Hola'
    return 'No encontrado'

@app.route('/face', methods=['GET', 'POST'])
def recognize_emotions():
  return(capture_and_detect_emotions())
  
@app.route('/voice', methods=['GET', 'POST'])
def greets():  # Saludamos al usuario
  engine = pyttsx3.init()
  voices = engine.getProperty('voices')

  # Seleccionar una voz diferente (en este caso, la primera de la lista)
  engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
  engine.setProperty('voice', voices[0].id) 

  engine.say("Hola, soy Jarvis TEC su asistente personal. ¿Qué modelo quiere usar?")
  engine.runAndWait()

  engine.say(menu)
  engine.runAndWait()
  # Mostramos el menú de opciones
  # jarvisSay(menu)

  while True:
    # Intentamos reconocer la voz del usuario
    response = recognize_audio()

    # Reproducimos la respuesta del usuario
    engine.say(response["data"])
    engine.runAndWait()

    # Si ha entendido el mensaje, salimos del bucle
    if(response["message_understood"] == True):
      break;
  return 'OK'

if __name__ == '__main__':
    app.run(debug=True)

#Opción 1 -> 2017/08/08
#Opción 2 -> 3/15000/50000/Gasolina/Consecionario/Manual/1
#Opción 3 -> Tom and Huck/5
#Opción 4 -> 8.9/0.3/0.38/2.8/0.10/31/69/0.998/3.25/0.86/12.8/1/0
#Opción 5 -> Aliss/3/5/2024
#Opción 6 -> 1.0/0.5/3.2/2/0.0/Tarjeta de crédito/estándar/0.5/0.3
#Opción 7 -> Masculino/No/No/No/56/Si/Si/Si/Fiber optic/Si/Si/Si/Si/Si/Si/Two year/Si/Credit card (automatic)/110.50/6230
#Opción 8 -> 1853.0/520/1439.0/1234/fl/172.0/84.0/235.0/48.0/22.0/1230/22.0/0/2.0/11.0
#Opción 9 -> 1.0/3/50.0/100.0/20.0/50.0/40.0/30.0/20.0/15.0/10.0/15.0/10.0/8.0
#Opción 10 -> 100.9/60.2/30.6/10.1/150.6/100.4/50.2/0.0/2/2023/San Diego