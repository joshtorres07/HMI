import socket
import json

# Crear un socket
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Dirección y puerto del servidor
host = "localhost"  # Cambia esto a la dirección del servidor si es necesario
port = 10000

# Conectar al servidor
ss.connect((host, port))

# Solicitar al usuario ingresar una lista de números
user_input = input("Ingrese una lista de números separados por comas (por ejemplo, 1,2,3): ")
user_list = [int(x) for x in user_input.split(",")]

# Convertir la lista en JSON
user_list_json = json.dumps(user_list)

# Enviar la lista al servidor
ss.send(user_list_json.encode("utf-8"))

# Recibir la lista del servidor
lista_modificada_json = ss.recv(1024).decode("utf-8")

# Convertir la lista modificada JSON en una lista de Python
lista_modificada = json.loads(lista_modificada_json)

# Cerrar la conexión
ss.close()

# Mostrar la lista
print(f"\nLa lista es: {lista_modificada}")
