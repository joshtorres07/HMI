#cliente hilo
import socket
host ='localhost'
pto=5000
msg = input ("mensaje")
cservidor = socket.socket()
cservidor.connect((host, pto))
while msg != 'exit':
    cservidor.send(msg.encode())
    d= cservidor.recv(2048)
    print("recivbio: ",d.decode())
    msg= input("nuevo mensaje, exit para terminarlo")
cservidor.close()
    
