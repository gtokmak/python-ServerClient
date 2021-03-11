import socket
import threading
import time

PORT = 7777
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect((socket.gethostname(), PORT))

while True:
    clientSock.send(bytes("openBarrier", "utf-8"))
    msg = clientSock.recv(1024)
    print(msg.decode('utf-8'))
    time.sleep(1)
    clientSock.send(bytes("closeBarrier", "utf-8"))
    msg = clientSock.recv(1024)
    print(msg.decode('utf-8'))
    time.sleep(1)
