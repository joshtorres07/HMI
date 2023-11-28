import speech_recognition as sr

# Cargar el archivo de audio
audio_file = "miarchivo.wav"

# Inicializar el reconocedor
recognizer = sr.Recognizer()

# Leer el audio desde el archivo
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)

# Intentar la transcripción
try:
    text = recognizer.recognize_google(audio_data, language="es")
    print("Texto transcribido: ", text)
except sr.UnknownValueError:
    print("No se pudo entender el audio")
except sr.RequestError as e:
    print("Error en la solicitud a la API de Google: {0}".format(e))
