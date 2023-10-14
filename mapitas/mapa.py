

#Geolocalización
from geopy.geocoders import Nominatim
import time
import math

#Dibujar mapas
import matplotlib.pyplot as plt
import  mpl_toolkits
from mpl_toolkits.basemap import Basemap

geolocator = Nominatim(user_agent="AppMap")

location = geolocator.geocode("Tecnologico Ciudad Guzman")
print(location.address)

#Dimensiónd de la figura
plt.figure(figsize=(16,12))

#Distribución lines costeras
eq_map=Basemap(projection='robin',lon_0=0,lat_0=0)

#Dibujar lineas costeras y paises
eq_map.drawcoastlines()
eq_map.drawcountries()

#Definir colores
eq_map.fillcontinents(color="brown")
eq_map.drawmapboundary(fill_color="aqua")

#Situo el lugar en el mapa
x,y = eq_map(location.longitude,location.latitude)
eq_map.plot(x,y, "ro", markersize=17, alpha=0.8)
plt.savefig("mapa.png", dpi=300)  # Cambia "mapa.png" al nombre de archivo que desees y ajusta la resolución según tus necesidades
plt.show()