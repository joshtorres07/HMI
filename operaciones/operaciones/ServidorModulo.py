import socket
import json

operations_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
operations_server_address = ('localhost', 30005)
print("Iniciando servidor de modulo")

operations_server_socket.bind(operations_server_address)

while True:
    print("En espera de los números")
    data, adr = operations_server_socket.recvfrom(4046)
    print('Recibido', len(data), 'bytes', adr)

    try:
        numeros = json.loads(data.decode())

        if len(numeros) == 3:
            resultado = numeros[1] % numeros[2]  # Modulo
            print("Resultado enviado de vuelta al cliente:", resultado)
            operations_server_socket.sendto(json.dumps(resultado).encode(), adr)  # Enviar respuesta al cliente
        else:
            print("Los datos recibidos no son válidos:", numeros)
            resultado = 0
            operations_server_socket.sendto(json.dumps(resultado).encode(), adr)  # Enviar respuesta al cliente
    except json.JSONDecodeError:
        print("Error al decodificar los datos JSON recibidos")
    except Exception as e:
        print("Error:", e)
operations_server_socket.close()
