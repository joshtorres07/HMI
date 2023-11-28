import webbrowser  #Para abrir el navegador
import speech_recognition as sr
import os

r= sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print ("Hola soy tu asistente, que servicio deseas?")
        audio = r.listen(source)
        try:
            text= r.recognize_google(audio)
            print(f'has dicho: {text}')
            if "hola"in text:
                print("holaa")
            if "Amazon" in text:
                webbrowser.open("https://amazon.com.mx")
            if "tec" in text:
                webbrowser.open("https://cdguzman.tecnm.mx")
            if "aplicacion" in text:
                os.system("start Menu.py")
            if "adios" in text:
                print("hasta luego")
                break
        except:
            print("No entiendo")