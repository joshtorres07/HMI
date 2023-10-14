import socket
import json
s = socket.socket()
port = 1235
s.connect(('127.0.0.1', port))
print(s.recv(1024).decode())
s.send(json.dumps((1,2,3,4,5,6)).encode())
x = s.recv(1024).decode()
print(x, type(x))
s.close()
input("press enter to finish")