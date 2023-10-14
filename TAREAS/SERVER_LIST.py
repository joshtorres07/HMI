import socket

# Crear un socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dirección y puerto del servidor
host = "localhost"
port = 10000

# Enlazar el socket al puerto y comenzar a escuchar
ss.bind((host, port))
ss.listen(1)

print(f"El servidor está escuchando en {host}:{port}")

# Aceptar una conexión entrante
cliente, addr = ss.accept()
print(f"Conexión entrante desde {addr}")

# Recibir la lista del cliente
lista_json = cliente.recv(1024).decode("utf-8")

# Convertir la lista JSON en una lista de Python
import json
lista = json.loads(lista_json)

# Convertir la lista modificada en JSON
lista_modificada_json = json.dumps(lista)

# Enviar la lista modificada al cliente
cliente.send(lista_modificada_json.encode("utf-8"))

# Cerrar la conexión
cliente.close()
