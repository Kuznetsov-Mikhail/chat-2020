import socket
import threading
import sys
import time

triger = True
def read_mess_from_server():
    while triger is True:
        try:
            data = sock.recv(1024)
            print(data.decode('utf-8'))
        except ConnectionResetError:
            continue
    sys.exit(0)

if __name__ == '__main__':
    server = '', 8080
    print('input nickname: ')
    name = str(input())
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sock.bind(('192.168.1.38', 0))
    sock.bind(('', 0))
    sock.sendto((name +' connect').encode('utf-8'), server)
    thr = threading.Thread(target=read_mess_from_server)
    thr.start()
    while True:
        try:
            mess = str(input())        
            sock.sendto(('[' + name + ']' + mess).encode('utf-8'), server)
            if 'exit' in mess:
                triger = False
                sys.exit(0)
        except ConnectionResetError:
            continue
