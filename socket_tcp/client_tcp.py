
import socket

sock = socket.socket()
sock.connect(('192.168.9.156', 8080))

while True:
    print("Enter your message or exit:")
    msg = raw_input()
    #Message = 'MyMSG'
    if (msg == 'exit'): 
        break
    sock.send(str(msg))
    data = sock.recv(1024)
    #sock.close()
    print data
    
