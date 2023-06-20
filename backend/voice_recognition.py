import speech_recognition as sr
# from voice import *
from voice_recognition import *
from options import select_model
from ia_models import *
import pyttsx3
from audio_to_text import process_audio

#pip install SpeechRecognition
#pip install pyaudio

# Rutas donde se guardarán los archivos de audio y texto
audio_path = "D:/crist/TEC/Semestre 7/INTELIGENCIA ARTIFICIAL/Proyecto 2/audios"
text_path = "D:/crist/TEC/Semestre 7/INTELIGENCIA ARTIFICIAL/Proyecto 2/text"

# Crear objeto de reconocimiento de voz
r = sr.Recognizer()

# Función para guardar el audio
def save_audio(audio):
  files = os.listdir(audio_path)
  number_files = len(files)
  audio_name = "audio" + str(number_files + 1)

  # Guardar el audio en la computadora
  os.makedirs(audio_path, exist_ok=True)
  audio_file = os.path.join(audio_path, audio_name + ".wav")
  with open(audio_file, "wb") as f:
    f.write(audio.get_wav_data())

  return audio_name

# Función para guardar el texto
def save_text(text):
  files = os.listdir(text_path)
  number_files = len(files)
  audio_name = "audio" + str(number_files + 1)

  # Guardar el archivo de texto con el identificador único
  text_file = os.path.join(text_path, audio_name + ".txt")
  with open(text_file, "w") as file:
    file.write(text)

# Función para reconocer el audio y devolver una respuesta
def recognize_audio():
  # Configurar el micrófono como fuente de audio
  with sr.Microphone() as source:
    print("Grabando")
    audio = r.listen(source)
  print("Dejé de grabar")

  try:
    # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
    audio_name = save_audio(audio);
    new_audio_path = audio_path + audio_name + ".wav"
    text = process_audio(new_audio_path)
    
    print("Ha dicho: " + text)

    # Guarda texto y audio
    save_text(text);

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
            # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
       
            audio_name = save_audio(audio);
            new_audio_path = audio_path + audio_name + ".wav"
            text = process_audio(new_audio_path)
            print("Ha dicho: " + text)
            
            # Guarda texto y audio
            save_text(text);

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
              # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
         
              audio_name = save_audio(audio);
              new_audio_path = audio_path + audio_name + ".wav"
              text = process_audio(new_audio_path)
              print("Ha dicho: " + text)
              text = text.replace(",", "")
              text = text.replace(".", "")

              # Guarda texto y audio
              save_text(text);

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
            # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
       
            audio_name = save_audio(audio);
            new_audio_path = audio_path + audio_name + ".wav"
            text = process_audio(new_audio_path)
            print("Ha dicho: " + text)

            # Guarda texto y audio
            save_text(text);

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
              # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
         
              audio_name = save_audio(audio);
              new_audio_path = audio_path + audio_name + ".wav"
              text = process_audio(new_audio_path)
              print("Ha dicho: " + text)

              # Guarda texto y audio
              save_text(text);

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
              # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
         
              audio_name = save_audio(audio);
              new_audio_path = audio_path + audio_name + ".wav"
              text = process_audio(new_audio_path)
              print("Ha dicho: " + text)

              # Guarda texto y audio
              save_text(text);

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
              # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
         
              audio_name = save_audio(audio);
              new_audio_path = audio_path + audio_name + ".wav"
              text = process_audio(new_audio_path)
              print("Ha dicho: " + text)

              # Guarda texto y audio
              save_text(text);

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
                    # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
               
                    audio_name = save_audio(audio);
                    new_audio_path = audio_path + audio_name + ".wav"
                    text = process_audio(new_audio_path)
                    print("Ha dicho: " + text)

                    # Guarda texto y audio
                    save_text(text);

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
                  # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
             
                  audio_name = save_audio(audio);
                  new_audio_path = audio_path + audio_name + ".wav"
                  text = process_audio(new_audio_path)
                  print("Ha dicho: " + text)

                  # Guarda texto y audio
                  save_text(text);

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
              # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
         
              audio_name = save_audio(audio);
              new_audio_path = audio_path + audio_name + ".wav"
              text = process_audio(new_audio_path)
              print("Ha dicho: " + text)

              # Guarda texto y audio
              save_text(text);

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
              # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
         
              audio_name = save_audio(audio);
              new_audio_path = audio_path + audio_name + ".wav"
              text = process_audio(new_audio_path)
              print("Ha dicho: " + text)

              # Guarda texto y audio
              save_text(text);

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
              # text = r.recognize_google(audio, language="es-ES") # Convertir el audio en texto usando el servicio de reconocimiento de voz de Google
         
              audio_name = save_audio(audio);
              new_audio_path = audio_path + audio_name + ".wav"
              text = process_audio(new_audio_path)
              print("Ha dicho: " + text)

              # Guarda texto y audio
              save_text(text);

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