import socket
import json

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ('localhost', 20000)
print("Iniciando servidor")

ss.bind(address)

while True:
    print("En espera de los números")
    data, adr = ss.recvfrom(4046)
    print('Recibido', len(data), 'bytes', adr)

    try:
        numeros = json.loads(data.decode())
        if isinstance(numeros, list) and len(numeros) == 3:
            resultado = numeros[0] - numeros[1]
            resultado_json = json.dumps(resultado)
            ss.sendto(resultado_json.encode(), adr)
            print("Resultado enviado de vuelta al cliente:", resultado)
        else:
            print("Los datos recibidos no son válidos:", numeros)
    except json.JSONDecodeError:
        print("Error al decodificar los datos JSON recibidos")
    except Exception as e:
        print("Error:", e)

ss.close()
