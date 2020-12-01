import socket

sock = socket.socket()
sock.connect(('localhost', 8000))

while True:
    print("Enter your message or exit:")
    msg = raw_input()
    if (msg == 'exit'): 
        break
    sock.send(str(msg))
    data = sock.recv(1024)
    #sock.close()
    print(data)
