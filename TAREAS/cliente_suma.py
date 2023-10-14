# programa cliente
# TORRES SANTOSJOSUE DANIEL

import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 10000
ss.connect(("localhost", port))

num1 = input("INPUT THE FIRST NUMBER: ")
ss.send(num1.encode("ascii"))

num2 = input("ENTER THE SECOND NUMBER ")
ss.send(num2.encode("ascii"))

msg = ss.recv(1024)
ss.close()
print(f"\nLa suma da: {msg.decode('ascii')}")
