# Programa servidor
# TORRES SANTOSJOSUE DANIEL

import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
cont = 0
port = 10000
ss.bind(("localhost", port))
ss.listen(5)

while True:
    cs, addr = ss.accept()
    print("IT LOOKS GOOD", str(addr))

    num1 = cs.recv(1024).decode("ascii")
    num2 = cs.recv(1024).decode("ascii")
    suma = str(int(num1) + int(num2))

    cs.send(suma.encode("ascii"))
    cont += 1
    if cont > 5:
        print("YOU REACHED YOUR LIMIT")
        break

ss.close()
input("ENTER TO FINISH")
