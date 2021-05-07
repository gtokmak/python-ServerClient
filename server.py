import time
import socket
import threading

HOST = "127.0.0.1"
PORT = 7777

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_UNIX: UNIX domain protokolleri
# AF_INET: TCP ve UDP için IPv4 protokolleri
# AF_INET6: TCP ve UDP için IPv6 protokolleri
# SOCK_STREAM: TCP bağlantı tipi
# SOCK_DGRAM: UDP bağlantı tipi
# SOCK_RAW: Henüz olgunlaşmamış soketler
# SOCK_RDM: Güvenilir datagramlar için
# SOCK_SEQPACKET: Bağlantı üzerinden kayıtlar için bir dizi transfer.

sock.bind((HOST, PORT))
sock.listen(3) # aynı anda en fazla bağlantıya verilecek sayı
connections =[]


def handler(clientSocket, address):
    global connections
    while True:
        data = clientSocket.recv(1024).decode("utf-8")
        if data == "openBarrier":
            clientSocket.send(bytes("The barrier is opened.", "utf-8"))
        if data == "closeBarrier":
            clientSocket.send(bytes("The barrier is closed.", "utf-8"))
        print(data)
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
    print_info(f'Soket uygulamasi IP:{HOST}, PORT:{PORT}')
    while True:
        clientSocket, address = sock.accept()
        cThread = threading.Thread(target=handler, args=(clientSocket, address))
        cThread.daemon = True
        cThread.start()
        connections.append(clientSocket)
        print(connections)

