import socket
import json

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor_adr = ('localhost', 20000)
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese el segundo numero: "))
numeros = (n1, n2, n3)


def suma(numeros):
    try:
        numeros_json = json.dumps(numeros)

        print("Enviando números al servidor")
        ss.sendto(numeros_json.encode(), servidor_adr)

        print("Esperando respuesta")
        dato, adr = ss.recvfrom(4046)
        resultado = json.loads(dato.decode())

        print("El resultado de la suma es", resultado)
    finally:
        print("Cerrando socket cliente")
        ss.close()

input("Presione Enter para terminar")
