import speech_recognition as sr
# from voice import *
from voice_recognition import *
from options import select_model
from ia_models import *
import pyttsx3


#pip install SpeechRecognition
#pip install pyaudio

# Crear objeto de reconocimiento de voz
r = sr.Recognizer()

# Definir una función para reconocer el audio y devolver una respuesta
def recognize_audio():
  # Configurar el micrófono como fuente de audio
  with sr.Microphone() as source:
    print("Grabando")
    audio = r.listen(source)
  print("Dejé de grabar")

  try:
    text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
    print("Ha dicho: " + text)

    # Seleccionar la respuesta apropiada basándose en el texto reconocido
    response = select_model(text)

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Seleccionar una voz diferente (en este caso, la primera de la lista)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
    engine.setProperty('voice', voices[2].id) 

    if (response == "Lo siento, no he entendido su respuesta. Por favor, seleccione una opción válida."):
      return {"data": response, "message_understood": False}
    elif(response['id'] == 1):
      date = ''
      engine.say(response['messages'][0])
      engine.runAndWait()
      for message in response['messages'][1:]:
        while True:
          engine.say(message)
          engine.runAndWait()
          with sr.Microphone() as source:
            print("Grabando")
            audio = r.listen(source)
          print("Dejé de grabar")

          try:
            text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
            print("Ha dicho: " + text)
            if(text ==  'uno'):
              text = '1'
            elif(text == 'iess'):
              text = '10'
            if(date == ''):
              date = text
            else:
              date = date + '-' + text
            break
          except sr.UnknownValueError:
            engine.say("No se ha podido entender lo que ha dicho")
            engine.runAndWait()
          except sr.RequestError as e:
            engine.say("Error al intentar reconocer la voz: " + e)
            engine.runAndWait()
      return {"data": precioBitcoin(date), "message_understood": True}


    elif(response['id'] == 2):
      while True:
        data = []
        engine.say(response['messages'][0])
        engine.runAndWait()
        for message in response['messages'][1:]:
          while True:
            engine.say(message)
            engine.runAndWait()
            with sr.Microphone() as source:
              print("Grabando")
              audio = r.listen(source)
            print("Dejé de grabar")

            try:
              text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
              print("Ha dicho: " + text)
              if(text ==  'uno'):
                text = '1'
              elif(text ==  'iess'):
                text = '10'
              text = text.replace(",", "")
              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
        try:      
          return {"data": precioAutomovil(int(data[0]), int(data[1]), int(data[2]), data[3], data[4], data[5], int(data[6])), "message_understood": True}
        except ValueError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()

    elif(response['id'] == 3):
      data = []
      engine.say(response['messages'][0])
      engine.runAndWait()
      for message in response['messages'][1:]:
        while True:
          engine.say(message)
          engine.runAndWait()
          with sr.Microphone() as source:
            print("Grabando")
            audio = r.listen(source)
          print("Dejé de grabar")

          try:
            text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
            print("Ha dicho: " + text)
            if(text ==  'uno'):
              text = '1'
            elif(text ==  'iess'):
                text = '10'
            data.append(text)
            break
          except sr.UnknownValueError:
            engine.say("No se ha podido entender lo que ha dicho")
            engine.runAndWait()
          except sr.RequestError as e:
            engine.say("Error al intentar reconocer la voz: " + e)
            engine.runAndWait()
      return {"data": recomendarPelicula(data[0], data[1]), "message_understood": True}
    
    elif(response['id'] == 4):
      while True:
        data = []
        engine.say(response['messages'][0])
        engine.runAndWait()
        for index, message in enumerate(response['messages'][1:]):
          while True:
            engine.say(message)
            engine.runAndWait()
            with sr.Microphone() as source:
              print("Grabando")
              audio = r.listen(source)
            print("Dejé de grabar")

            try:
              text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
              print("Ha dicho: " + text)
              if(text ==  'uno'):
                text = '1'
              elif(text ==  'iess'):
                text = '10'
              text = text.replace(",", ".")
              if(index == 11):
                if(text == 'rojo'):
                  data.append(1)
                  data.append(0)
                else:
                  data.append(0)
                  data.append(1)
              else:
                data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
        try:
          return {"data": calidadVino(float(data[0]), float(data[1]), float(data[2]), float(data[3]), float(data[4]), int(data[5]), int(data[6]), 
                                    float(data[7]), float(data[8]), float(data[9]), float(data[10]), int(data[11]), int(data[12])), "message_understood": True}
        except ValueError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()

    elif(response['id'] == 5):
      while True:
        data = []
        engine.say(response['messages'][0])
        engine.runAndWait()
        for index, message in enumerate(response['messages'][1:]):
          while True:
            engine.say(message)
            engine.runAndWait()
            with sr.Microphone() as source:
              print("Grabando")
              audio = r.listen(source)
            print("Dejé de grabar")

            try:
              text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
              print("Ha dicho: " + text)
              if(text ==  'uno'):
                text = '1'
              elif(text ==  'iess'):
                text = '10'
              elif(text == 'Alice'):
                text = 'Aliss'
              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
        try:
          return {"data": cantidadInventario(data[0], int(data[1]), int(data[2]), int(data[3])), "message_understood": True}
        except ValueError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()

    elif(response['id'] == 6):
      while True:
        data = []
        engine.say(response['messages'][0])
        engine.runAndWait()
        for index, message in enumerate(response['messages'][1:]):
          while True:
            engine.say(message)
            engine.runAndWait()
            with sr.Microphone() as source:
              print("Grabando")
              audio = r.listen(source)
            print("Dejé de grabar")

            try:
              text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
              print("Ha dicho: " + text)
              if(text ==  'uno'):
                text = '1'
              elif(text ==  'iess'):
                text = '10'
              text = text.replace(",", ".")
              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
        try:
          return {"data": tarifaTaxi(float(data[0]), float(data[1]), float(data[2]), int(data[3]), float(data[4]), data[5], data[6], float(data[7]), float(data[8])), "message_understood": True}
        except ValueError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()

    elif(response['id'] == 7):
      while True:
        data = []
        engine.say(response['messages'][0])
        engine.runAndWait()
        for index, message in enumerate(response['messages'][1:]):
            if index > 7 and index <= 14:
              if data[7] == 'si':
                while True:
                  engine.say(message)
                  engine.runAndWait()
                  with sr.Microphone() as source:
                    print("Grabando")
                    audio = r.listen(source)
                  print("Dejé de grabar")
                  print('si tiene internet')
                  try:
                    text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
                    print("Ha dicho: " + text)
                    if(text ==  'uno'):
                      text = '1'
                    elif(text ==  'iess'):
                      text = '10'
                    elif(text ==  'sí'):
                      text = 'si'
                    text = text.replace(",", ".")
                    data.append(text)
                    break
                  except sr.UnknownValueError:
                    engine.say("No se ha podido entender lo que ha dicho")
                    engine.runAndWait()
                  except sr.RequestError as e:
                    engine.say("Error al intentar reconocer la voz: " + e)
                    engine.runAndWait()
              else:
                print('no tiene internet')
                data.append('sin servicio de internet')
            else:
              while True:
                engine.say(message)
                engine.runAndWait()
                with sr.Microphone() as source:
                  print("Grabando")
                  audio = r.listen(source)
                print("Dejé de grabar")
                try:
                  text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
                  print("Ha dicho: " + text)
                  if(text ==  'uno'):
                    text = '1'
                  elif(text ==  'iess'):
                    text = '10'
                  elif(text ==  'sí'):
                    text = 'si'
                  text = text.replace(",", ".")
                  data.append(text)
                  break
                except sr.UnknownValueError:
                  engine.say("No se ha podido entender lo que ha dicho")
                  engine.runAndWait()
                except sr.RequestError as e:
                  engine.say("Error al intentar reconocer la voz: " + e)
                  engine.runAndWait()
        try:
          return {"data": clienteCompañiaCelular(data[0], data[1], data[2], data[3], int(data[4]), data[5], data[6], 
                                                data[8], data[9], data[10], data[11], data[12], data[13], data[14], 
                                                data[15], data[16], data[17], float(data[18]), float(data[19])), "message_understood": True}
        except ValueError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()

    elif(response['id'] == 8):
      while True:
        data = []
        engine.say(response['messages'][0])
        engine.runAndWait()
        for index, message in enumerate(response['messages'][1:]):
          while True:
            engine.say(message)
            engine.runAndWait()
            with sr.Microphone() as source:
              print("Grabando")
              audio = r.listen(source)
            print("Dejé de grabar")

            try:
              text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
              print("Ha dicho: " + text)
              if(text ==  'uno'):
                text = '1'
              elif(text ==  'iess'):
                text = '10'
              text = text.replace(",", ".")
              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
        try:
          return {"data": delayViajeAvion(float(data[0]), int(data[1]), float(data[2]), int(data[3]), data[4], float(data[5]), 
                                          float(data[6]), float(data[7]), float(data[8]), float(data[9]), int(data[10]),
                                          float(data[11]), int(data[12]), float(data[13]), float(data[14])), "message_understood": True}
        except ValueError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()

    elif(response['id'] == 9):
      while True:
        data = []
        engine.say(response['messages'][0])
        engine.runAndWait()
        for index, message in enumerate(response['messages'][1:]):
          while True:
            engine.say(message)
            engine.runAndWait()
            with sr.Microphone() as source:
              print("Grabando")
              audio = r.listen(source)
            print("Dejé de grabar")

            try:
              text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
              print("Ha dicho: " + text)
              if(text ==  'uno'):
                text = '1'
              elif(text ==  'iess'):
                text = '10'
              text = text.replace(",", ".")
              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
        try:
          return {"data": masaCorporal(float(data[0]), int(data[1]), float(data[2]), float(data[3]), float(data[4]), float(data[5]), 
                                          float(data[6]), float(data[7]), float(data[8]), float(data[9]), float(data[10]),
                                          float(data[11]), float(data[12]), float(data[13])), "message_understood": True}
        except ValueError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()
    
    elif(response['id'] == 10):
      while True:
        data = []
        engine.say(response['messages'][0])
        engine.runAndWait()
        for index, message in enumerate(response['messages'][1:]):
          while True:
            engine.say(message)
            engine.runAndWait()
            with sr.Microphone() as source:
              print("Grabando")
              audio = r.listen(source)
            print("Dejé de grabar")

            try:
              text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
              print("Ha dicho: " + text)
              if(text ==  'uno'):
                text = '1'
              elif(text ==  'iess'):
                text = '10'
              text = text.replace(",", ".")
              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
        try:
          return {"data": precioAguacate(float(data[0]), float(data[1]), float(data[2]), float(data[3]), float(data[4]), float(data[5]), 
                                          float(data[6]), float(data[7]), int(data[8]), int(data[9]), data[10]), "message_understood": True}
        except ValueError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()    

  except sr.UnknownValueError:
    message = "No se ha podido entender lo que ha dicho"
    return {"data": message, "message_understood": False}
  except sr.RequestError as e:
    message = "Error al intentar reconocer la voz: " + e
    return {"data": message, "message_understood": False}