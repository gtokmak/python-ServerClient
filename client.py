import socket
import threading


PORT = 7777
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), PORT))

while True:
    msg = sock.recv(1024)
    print(msg.decode('utf-8'))
