import  speech_recognition as sr
import os
r = sr.Recognizer()

with sr.AudioFile("versionWav.wav") as source:
    audio = r.record(source)

os.system("start versionWav.wav")
texto = r.recognize_google(audio, language='es-Es')
print(texto)

