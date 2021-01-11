import socket
import requests
import subprocess
import time

print("Server started... ")
sock = socket.socket()
def connection(sock):
    sock.bind(('', 9999))
    sock.listen(1)
    conn, addr = sock.accept()
    return conn, addr
conn, addr = connection(sock)

print('connected:', addr)
triger = True
while True:
    try:
        if triger is True: 
            data = conn.recv(1024)
        if 'exit done' in data:
            print("client: closed")
            conn.close()
            break
        if triger is True: 
            print(str(addr) + ": " + data)
        print("Enter your message or exit: ")
        msg = raw_input()
        if (msg == 'exit'):
            conn.send(str("exit done"))
            conn.close() 
            break

        response = requests.get('http://www.google.com')
        #output = subprocess.check_output('ping 192.168.1.213')
        #print(output)

        triger = True
        conn.send("server: " + msg)
    except requests.ConnectionError:
        print('ConnectionError')
        triger = False
    except socket.error or ConnectionResetError:
        conn.close()
        time.sleep(0.1)
        sock = socket.socket()
        conn, addr = connection(sock)
conn.close()