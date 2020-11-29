import socket
import threading

def read_mess_from_server():
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))


#####CLIENT##################
if __name__ == '__main__':
    server = '192.168.0.106', 9090
    print('input nickname: ')
    name = str(input())
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 0))
    sock.sendto((name +'connect').encode('utf-8'), server)
    thr = threading.Thread(target=read_mess_from_server)
    thr.start()
    while True:
        mess = str(input())
        sock.sendto(('[' + name + ']' + mess).encode('utf-8'), server)
