import numpy as np
import tensorflow as tf

# Definición de la función de pérdida CTC
def CTCLoss(y_true, y_pred):
    batch_len = tf.cast(tf.shape(y_true)[0], dtype="int64")
    input_length = tf.cast(tf.shape(y_pred)[1], dtype="int64")
    label_length = tf.cast(tf.shape(y_true)[1], dtype="int64")

    input_length = input_length * tf.ones(shape=(batch_len, 1), dtype="int64")
    label_length = label_length * tf.ones(shape=(batch_len, 1), dtype="int64")

    # Calcular la pérdida de CTC por lotes
    loss = tf.keras.backend.ctc_batch_cost(y_true, y_pred, input_length, label_length)
    return loss

# Cargar el modelo entrenado
model = tf.keras.models.load_model('./Modelos/traductorAudioTexto.h5', custom_objects={"CTCLoss": CTCLoss})

# Función para procesar el audio y convertirlo a texto
def process_audio(audio_path):
    # Preprocesar el audio
    processed_audio = preprocess_audio(audio_path)

    # Obtener la transcripción del audio usando el modelo
    predictions = model.predict(tf.expand_dims(processed_audio, axis=0))

    # Definición de las clases de salida
    characters = ['', 'h', 'y', 't', '4', 'm', 'i', 'o', '8', 'b', 'p', ',', 'k', '1', 'r', '3', 'd', '5', ' ', 'w', '2', 'c', '9', '0', 'g', 'l', '6', 'n', 'a', 'v', 'e', 'f', 'j', '.', '7', 'u', 's']

    # Mapear caracteres a enteros
    char_to_num = tf.keras.layers.StringLookup(vocabulary=characters, oov_token="")

    # Mapear enteros a caracteres originales
    num_to_char = tf.keras.layers.StringLookup(
        vocabulary=char_to_num.get_vocabulary(), oov_token="", invert=True
    )

    # Obtener el texto completo
    input_len = np.ones(predictions.shape[0]) * predictions.shape[1]
    # Usar búsqueda voraz (greedy search). Para tareas más complejas, se puede usar búsqueda en haz (beam search)
    results = tf.keras.backend.ctc_decode(predictions, input_length=input_len, greedy=True)[0][0]
    # Iterar sobre los resultados y obtener el texto
    output_text = []
    for result in results:
        result = tf.strings.reduce_join(num_to_char(result)).numpy().decode("utf-8")
        output_text.append(result)
    return output_text[0]

# Definir las variables de configuración del preprocesamiento
frame_length = 256
frame_step = 160
fft_length = 384

# Definir la función de preprocesamiento
def preprocess_audio(audio_path):
    # Cargar el archivo de audio
    audio = tf.io.read_file(audio_path)
    audio_tensor = tf.audio.decode_wav(audio, desired_channels=1)
    audio_data = tf.squeeze(audio_tensor.audio, axis=-1)
    # Cambiar el tipo a float32
    audio_data = tf.cast(audio_data, tf.float32)
    # Calcular el espectrograma
    spectrogram = tf.signal.stft(
        audio_data,
        frame_length=frame_length,
        frame_step=frame_step,
        fft_length=fft_length
    )
    # Calcular la magnitud del espectrograma
    spectrogram = tf.abs(spectrogram)
    spectrogram = tf.math.pow(spectrogram, 0.5)
    # Normaliza el espectrograma
    means = tf.math.reduce_mean(spectrogram, 1, keepdims=True)
    stddevs = tf.math.reduce_std(spectrogram, 1, keepdims=True)
    spectrogram = (spectrogram - means) / (stddevs + 1e-10)
    # Devolver el espectrograma preprocesado
    return spectrogram

# Ejemplo de uso
# audio_path = 'c:/Users/Personal/Desktop/TEC/Semestre 7/Inteligencia Artificial/Proyecto 2/audios/audio4.wav'
# text = process_audio(audio_path)
# print("Predicción:", text)
