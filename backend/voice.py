import pyttsx3

#pip install pyttsx3

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Obtener las voces disponibles en el sistema
voices = engine.getProperty('voices')

# Seleccionar una voz diferente (en este caso, la primera de la lista)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
engine.setProperty('voice', voices[0].id) 

def jarvisSay(message):
  # Hacer que el asistente diga el mensaje
  engine.say(message)
  # Esperar hasta que el mensaje haya sido completado
  engine.runAndWait()
