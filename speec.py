import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Dime algo")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

with open("versionWav.wav", "wb") as f:
    f.write(audio.get_wav_data())

with open("versionRaw.raw", "wb") as f:
    f.write(audio.get_raw_data())

with open("versionAIFF.aiff", "wb") as f:
    f.write(audio.get_aiff_data())

with open("versionFlac.flac", "wb") as f:
    f.write(audio.get_flac_data())
