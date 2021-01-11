import socket
import requests

sock = socket.socket()
sock.connect(('192.168.1.213', 8080))
print("Enter your name:")
name = raw_input()
name = str(name)+ ": "
while True:
    try:
        print("Enter your message or exit: ")
        msg = raw_input()
        if (msg == 'exit'):
            sock.send(str(name + "exit done"))
            sock.close() 
            break
        response = requests.get('https://www.google.com')
        sock.send(str(name + msg))
        data = sock.recv(1024)
        if 'exit done' in data:
            print("server: closed")
            sock.close()
            break
        print data

    except requests.ConnectionError or KeyboardInterrupt:
        print("ConnectionError")
sock.close()