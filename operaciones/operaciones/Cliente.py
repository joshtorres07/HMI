import socket
import json

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor_adr = ('10.32.103.154', 20000)
1
while True:
    operacion = input("Ingrese el tipo de operacion\n1.- Suma\n2.- Resta\n3.- Multiplicacion\n4.- Division\n5.- Potencia\n6.- Modulo\n7.- Salir\nNumero de operacion: ")
    if operacion == '7':
        print("Saliendo del programa.")
        break 
    elif operacion not in ('1', '2', '3', '4', '5', '6'):
        print("Operación no válida. Intente de nuevo.")
        continue
    n1 = int(input("Ingrese el primer numero: "))    
    while True:
        n2 = int(input("Ingrese el segundo numero: "))
        if n2 ==0 and operacion == '4':
            print("El segundo número no puede ser 0. Intente de nuevo.")
        else:
            break
    numeros = (int(operacion), n1, n2)
    try:
        numeros_json = json.dumps(numeros)

        print("Enviando números al servidor")
        cliente_socket.sendto(numeros_json.encode(), servidor_adr)

        print("Esperando respuesta")
        dato, adr = cliente_socket.recvfrom(4046)
        resultado = json.loads(dato.decode())

        print("El resultado es", resultado)
    except Exception as e:
        print("Error:", e)
        break
print("Cerrando socket cliente")
cliente_socket.close()
