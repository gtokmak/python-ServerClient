import time
import socket
import threading

HOST = '0.0.0.0'
PORT = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.AF_INET IPv4
#socket.AF_INET6 IPv6
#socket.SOCK_STREAM TcpIp
#socket.SOCK_DGRAM UDP

sock.bind((socket.gethostname(), PORT))
sock.listen(1)
connections =[]


def handler(clientSocket, address):
    global connections
    while True:
        data = clientSocket.recv(1024)
        for connection in connections:
            #connection.send(bytes(data))
            time.sleep(0.1)
            connection.send(bytes("Welcome to server!\r\n", "utf-8"))
        if not data:
            connections.remove(clientSocket)
            print(f'close connection {clientSocket}')
            clientSocket.close()
            break



def print_info(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'{name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_info(f'Soket uygulamasi IP:{HOST}, PORT:{PORT} ile basladi')
    while True:
        clientSocket, address = sock.accept()
        cThread = threading.Thread(target=handler, args=(clientSocket, address))
        cThread.daemon = True
        cThread.start()
        connections.append(clientSocket)
        print(connections)

