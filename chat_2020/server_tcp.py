import socket
sock = socket.socket()
sock.bind(('', 8080))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', str(addr))
count = 0
while True:
    data = conn.recv(1024)
    if not data:
        continue
    else:
        print('Message from ' + str(addr) + ":")
        print(data)
        conn.send(data.upper())
        
conn.close()