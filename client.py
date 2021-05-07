import socket
import threading
import time

PORT = 3001
HOST = "127.0.0.1"
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((HOST, PORT))

while True:
    clientSock.send(bytes("Mesaj1", "utf-8"))
    msg = clientSock.recv(1024)
    print(msg.decode('utf-8'))
    time.sleep(1)
    clientSock.send(bytes("Mesaj2", "utf-8"))
    msg = clientSock.recv(1024)
    print(msg.decode('utf-8'))
    time.sleep(1)
