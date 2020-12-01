import socket

sock = socket.socket()
sock.bind(('', 8000))
sock.listen(1)
conn, addr = sock.accept()

print 'connected:', addr
count = 0
while True:
    data = conn.recv(1024)
    if not data:
        continue
    else:
        print('Message from ' + str(addr) + ":")
        print(data)
        msg = raw_input()
        if (msg == 'exit'): 
            break
        conn.send(str(msg))

conn.close()
