import socket
host  = "10.32.102.204"
port  = 12345
sct = socket.socket()
sct.connect((host,port))
print("Connecting with java server...")
while True:
    imp = input("Text to send: ")
    print("it will be send: "+ imp)
    sct.send(imp.encode("utf8"))
    rcv  = sct.recv(512)
    print("it have received: ", rcv.decode("utf8"))
    if imp == "exit":
        break
sct.close()
print("finished")