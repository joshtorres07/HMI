#Convertir Texto a audio
from gtts import gTTS
import os
"""
texto = "Hola buenos dias, espero que estes bien"
speech = gTTS(text = texto, lang = "es", slow = False)
speech.save("miarchivo.mp3")
os.system("start miarchivo.mp3") #funciona para abrir o ejecutar un archivo
"""

#convertir el texto a audio desde un archivo txt
texto = open("miTexto.txt", "r").read().replace("\n"," ")#Abrir un archivo de texto, el salto de linea lo remplaca por un espacio en blanco
speech = gTTS(text = texto, lang = "es", slow = False)
speech.save("miarchivo.mp3")
os.system("start miarchivo.mp3") #funciona para abrir o ejecutar un archivo