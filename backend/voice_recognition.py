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


# Función para reconocer el audio y devolver una respuesta
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
    engine.setProperty('voice', voices[0].id) 

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
              int(text)
              date = text
            else:
              int(text)
              date = date + '-' + text
            break
          except sr.UnknownValueError:
            engine.say("No se ha podido entender lo que ha dicho")
            engine.runAndWait()
          except sr.RequestError as e:
            engine.say("Error al intentar reconocer la voz: " + e)
            engine.runAndWait()
          except ValueError:
            engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
            engine.runAndWait()
      return {"data": precioBitcoin(date), "message_understood": True}

    elif(response['id'] == 2):
      while True:
        data = []
        engine.say(response['messages'][0])
        engine.runAndWait()
        for index, message in enumerate(response['messages'][1:]):
          while True:
            engine.say(message['message'])
            engine.runAndWait()
            with sr.Microphone() as source:
              print("Grabando")
              audio = r.listen(source)
            print("Dejé de grabar")

            try:
              text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
              print("Ha dicho: " + text)
              text = text.replace(",", "")
              text = text.replace(".", "")

              if(text ==  'uno'):
                text = '1'
              elif(text ==  'iess'):
                text = '10'

              if(message['type'] == 'str'):
                text = message['options'].get(text.lower(), 3)
                if text == 3: int('error')
              else:
                text = int(text)
              
              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
            except ValueError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
            except TypeError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
        try:      
          return {"data": precioAutomovil(data[0], data[1], data[2], data[3], data[4], data[5], data[6]), "message_understood": True}
        except ValueError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()
        except IndexError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()

    elif(response['id'] == 3):
      data = []
      engine.say(response['messages'][0])
      engine.runAndWait()
      movies = pd.read_csv('./Data/movies.csv')
      list_movies = movies["title"].tolist()
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

            if(index == 0):
              pelicula_existente = False
              for movie in list_movies:
                if text.lower() in movie.lower():
                  text = movie
                  pelicula_existente = True
                  break
              if(pelicula_existente == False):
                int('error')
            else:
              text = int(text)
            data.append(text)
            break
          except sr.UnknownValueError:
            engine.say("No se ha podido entender lo que ha dicho")
            engine.runAndWait()
          except sr.RequestError as e:
            engine.say("Error al intentar reconocer la voz: " + e)
            engine.runAndWait()
          except ValueError:
              if(index == 0):
                  engine.say("Ese nombre de la película no está registrado, por favor vuelva a intentar con otra película")
                  engine.runAndWait()
              else:
                engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
                engine.runAndWait()
          except TypeError:
            if(index == 0):
                engine.say("Ese nombre de la película no está registrado, por favor vuelva a intentar con otra película")
                engine.runAndWait()
            else:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
      return {"data": recomendarPelicula(data[0], data[1]), "message_understood": True}
    
    elif(response['id'] == 4):
      while True:
        data = []
        engine.say(response['messages'][0])
        engine.runAndWait()
        for message in response['messages'][1:]:
          while True:
            engine.say(message['message'])
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

              if(message['type'] == 'str'):
                text = message['options'].get(text.lower(), 2)
                if text == 2: 
                  int('error')
                elif text == 0:
                  data.append(1)
                  data.append(0)
                elif text == 1:
                  data.append(0)
                  data.append(1)
              else:
                text = float(text)
                data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
            except ValueError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
            except TypeError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
        try:
          return {"data": calidadVino(data[0], data[1], data[2], data[3], data[4], data[5], data[6], 
                                    data[7], data[8], data[9], data[10], data[11], data[12]), "message_understood": True}
        except ValueError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()

    elif(response['id'] == 5):
      while True:
        data = []
        engine.say(response['messages'][0])
        engine.runAndWait()
        for message in response['messages'][1:]:
          while True:
            engine.say(message['message'])
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

              if(message['type'] == 'str'):
                text = message['options'].get(text.lower(), 0)
                if text == 0: 
                  int('error')
              else:
                int(text)
              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
            except ValueError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
            except TypeError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
        try:
          return {"data": cantidadInventario(data[0], data[1], data[2], data[3]), "message_understood": True}
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
            engine.say(message['message'])
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

              if(message['type'] == 'str'):
                text = message['options'].get(text.lower(), 7)
                if text == 7: int('error')
              else:
                text = float(text)

              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
            except ValueError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
            except TypeError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
        try:
          return {"data": tarifaTaxi(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8]), "message_understood": True}
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
              if data[7] == 1:
                while True:
                  engine.say(message['message'])
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

                    if(message['type'] == 'str'):
                      text = message['options'].get(text.lower(), 4)
                      if text == 4: int('error')
                    elif(message['type'] == 'int'):
                      text = int(text)
                    else:
                      text = float(text)

                    data.append(text)
                    break
                  except sr.UnknownValueError:
                    engine.say("No se ha podido entender lo que ha dicho")
                    engine.runAndWait()
                  except sr.RequestError as e:
                    engine.say("Error al intentar reconocer la voz: " + e)
                    engine.runAndWait()
                  except ValueError:
                    engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
                    engine.runAndWait()
                  except TypeError:
                    engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
                    engine.runAndWait()
              else:
                data.append(0)
            else:
              while True:
                engine.say(message['message'])
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
                  
                  if(message['type'] == 'str'):
                    text = message['options'].get(text.lower(), 4)
                    if text == 4: int('error')
                  elif(message['type'] == 'int'):
                    text = int(text)
                  else:
                    text = float(text)

                  data.append(text)
                  break
                except sr.UnknownValueError:
                  engine.say("No se ha podido entender lo que ha dicho")
                  engine.runAndWait()
                except sr.RequestError as e:
                  engine.say("Error al intentar reconocer la voz: " + e)
                  engine.runAndWait()
                except ValueError:
                  engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
                  engine.runAndWait()
                except TypeError:
                  engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
                  engine.runAndWait()
        try:
          return {"data": clienteCompañiaCelular(data[0], data[1], data[2], data[3], data[4], data[5], data[6], 
                                                data[8], data[9], data[10], data[11], data[12], data[13], data[14], 
                                                data[15], data[16], data[17], data[18], data[19]), "message_understood": True}
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
            engine.say(message['message'])
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

              if(message['type'] == 'str'):
                text = message['options'].get(text.lower(), 0)
                if text == 0: int('error')
              elif(message['type'] == 'float'):
                text = float(text)
              else:
                text = int(text)

              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
            except ValueError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
            except TypeError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
        try:
          return {"data": delayViajeAvion(data[0], data[1], data[2], data[3], data[4], data[5], 
                                          data[6], data[7], data[8], data[9], data[10],
                                          data[11], data[12], data[13], data[14]), "message_understood": True}
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
            engine.say(message['message'])
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

              if(message['type'] == 'float'):
                text = float(text)
              else:
                text = int(text)
              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
            except ValueError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
            except TypeError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
        try:
          return {"data": masaCorporal(data[0], data[1], data[2], data[3], data[4], data[5], 
                                          data[6], data[7], data[8], data[9], data[10],
                                          data[11], data[12], data[13]), "message_understood": True}
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
            engine.say(message['message'])
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

              if(message['type'] == 'str'):
                text = message['options'].get(text.lower(), 55)
                if text == 55: int('error')
              elif(message['type'] == 'float'):
                text = float(text)
              else:
                text = int(text)

              data.append(text)
              break
            except sr.UnknownValueError:
              engine.say("No se ha podido entender lo que ha dicho")
              engine.runAndWait()
            except sr.RequestError as e:
              engine.say("Error al intentar reconocer la voz: " + e)
              engine.runAndWait()
            except ValueError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
            except TypeError:
              engine.say("El dato ingresado es incorrecto, por favor vuelva a brindar el dato")
              engine.runAndWait()
        try:
          return {"data": precioAguacate(data[0], data[1], data[2], data[3], data[4], data[5], 
                                          data[6], data[7], data[8], data[9], data[10]), "message_understood": True}
        except ValueError:
          engine.say("Uno de los datos es incorrecto, por favor vuelva a brindar los datos")
          engine.runAndWait()    

  except sr.UnknownValueError:
    message = "No se ha podido entender lo que ha dicho"
    return {"data": message, "message_understood": False}
  except sr.RequestError as e:
    message = "Error al intentar reconocer la voz: " + e
    return {"data": message, "message_understood": False}