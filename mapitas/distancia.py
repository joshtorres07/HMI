
from geopy.geocoders import Nominatim
import geopy.distance
import time
import math

app=Nominatim(user_agent="ITCG")
##Creamos función distancia para calcularla
def distancia(lugar1,lugar2):
    origen = app.geocode(lugar1)
    destino = app.geocode(lugar2)

    coord_origen=(origen.latitude,origen.longitude)
    coord_destino=(destino.latitude,destino.longitude)

    distancia = geopy.distance.distance(coord_origen,coord_destino)
    
    return print ("La distancia entre " + lugar1 + " y " + lugar2 + " es de " + str(distancia))

#Llamamos a la función
lugar1 = input ("Introduce ciudad de Origen: ")
lugar2 = input ("Introduce ciudad de Destino: ")
distancia(lugar1,lugar2)
