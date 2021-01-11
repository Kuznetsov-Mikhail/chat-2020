import socket
import time

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 8080))
    # while True:
    #     try:
    #         sock.bind(('', 8080))
    #         break
    #     except OSError:
    #         sock.close()
    #         time.sleep(0.5)
    #         sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    clients = []
    print('start server')
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            print('connected:', addr)
            if addr not in clients:
                clients.append(addr)
            if 'exit' in data.decode('utf-8'): clients.remove(addr)
            for client in clients:
                if client == addr:
                    continue
                sock.sendto(data, client)
        except ConnectionResetError: 
            continue
    sock.close()


if __name__ == '__main__':
    main()
