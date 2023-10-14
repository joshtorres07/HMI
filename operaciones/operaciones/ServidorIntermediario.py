import socket
import json

intermediate_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
intermediate_server_address = ('10.32.103.154', 20000)
operations_server_address_suma = ('localhost', 30000)
operations_server_address_resta = ('localhost', 30001)
operations_server_address_multiplicacion = ('localhost', 30002)
operations_server_address_division = ('localhost', 30003)
operations_server_address_potencia = ('localhost', 30004)
operations_server_address_modulo = ('localhost', 30005)

print("Iniciando servidor intermedio")

intermediate_server_socket.bind(intermediate_server_address)

while True:
    print("En espera de la Operacion")
    data, client_address = intermediate_server_socket.recvfrom(4046)
    print('Recibido', len(data), 'bytes', client_address)

    try:
        numeros = json.loads(data.decode())
        operacion = numeros[0]
        operations_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if operacion == 1:  # Suma
            print("Enviando números al servidor suma")
            operations_server_socket.sendto(json.dumps(numeros).encode(), operations_server_address_suma)  # Enviar la solicitud al servidor de suma
        elif operacion == 2:  # Resta
            print("Enviando números al servidor Resta")
            operations_server_socket.sendto(json.dumps(numeros).encode(), operations_server_address_resta)  # Enviar la solicitud al servidor de suma
        elif operacion == 3:  # Multiplicacion
            print("Enviando números al servidor Multiplicacion")
            operations_server_socket.sendto(json.dumps(numeros).encode(), operations_server_address_multiplicacion)
        elif operacion == 4:  # Division
            print("Enviando números al servidor Division")
            operations_server_socket.sendto(json.dumps(numeros).encode(), operations_server_address_division)
        elif operacion == 5:  # Potencia
            print("Enviando números al servidor Potencia")
            operations_server_socket.sendto(json.dumps(numeros).encode(), operations_server_address_potencia)
        elif operacion == 6:  # Modulo
            print("Enviando números al servidor Modulo")
            operations_server_socket.sendto(json.dumps(numeros).encode(), operations_server_address_modulo)
        print("Esperando respuesta")
        dato, server_inter_address = operations_server_socket.recvfrom(4046)  # Recibir respuesta del servidor
        print('Recibido', len(dato), 'bytes', server_inter_address)
        resultado = json.loads(dato.decode())
        print("Resultado enviado de vuelta al cliente:", resultado)
        intermediate_server_socket.sendto(json.dumps(resultado).encode(), client_address)            
    except json.JSONDecodeError:
        print("Error al decodificar los datos JSON recibidos")
    except Exception as e:
        print("Error:", e)

intermediate_server_socket.close()
