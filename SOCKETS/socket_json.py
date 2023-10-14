import socket
import  json
from io import StringIO

s = socket.socket()
port = 12345
s.bind(('', port))
s.listen(5)
print("ready to receive customers")
cont = 0
while True:
    c, addr = s.accept()
    cont += 1
    print("connecting...", addr)
    c.send("thanks for connecting, send your informartion".encode())
    #x =  c.recv(1024).decode()
    #ent = StringIO(x)
    #d = json.load(ent)
    x = c.recv(1024)
    d = json.loads(x.decode())
    print(d, type(d))
    for i,v in enumerate(d):
        d[i] = v**3
    print(d)
    c.send(json.dumps(d).encode())
    c.close()
    if cont == 5:
        s.close()
        break
input("press enter to finish")
