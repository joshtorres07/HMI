#servidor con hilo
import socket
from threading import Thread
class ClientThread(Thread):
    def __init__(self, ip, pto):
        Thread.__init__(self)
        self.ip=ip
        self.pto=pto
        print("servidor creado")
    def run(self):
        while True:
            d= conn.recv(2048)
            print('datos recibidos',d.decode())
            msg = input("hola , para terminar escribir exit ")
            if msg == 'exit':
                break
            conn.send(msg.encode())
iip = 'localhost'
ptoo=5000
servidor = socket.socket()
servidor.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
servidor.bind((iip,ptoo))
hilos=[]
while True:
    servidor.listen(4)
    print("en espera de clientes")
    (conn,(ip,pto))= servidor.accept()
    h= ClientThread(ip,pto)
    h.start()
    hilos.append(h)
for t in hilos:
    t.join()
    
    
        
