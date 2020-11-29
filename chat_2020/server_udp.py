import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 9090))
    clients = []
    print('start server')
    while True:
        data, addr = sock.recvfrom(1024)
        print('connected:', addr)
        if addr not in clients:
            clients.append(addr)
        for client in clients:
            if client == addr:
                continue
            sock.sendto(data, client)
    sock.close()


######SERVER##############
if __name__ == '__main__':
    main()
