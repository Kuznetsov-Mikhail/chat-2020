import time
import socket
from threading import Thread




#sock2 = socket.socket()
#sock2.listen(1)
#conn, addr = sock2.accept()

class MyThreadListen(Thread):
    
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.sock = socket.socket()
        self.sock.connect(('192.168.9.155', 8000))
    
    def run(self):
        print("thread listen:")
        self.sock.listen(1)

        while True:
            data = self.sock.recv(1024)
            print (data)



class MyThreadSend(Thread):
    
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        self.sock = socket.socket()
        self.sock.connect(('192.168.9.155', 8080))
    
    def run(self):
        print("thread send:")

        while True:
            print("Enter your message or exit:")
            msg = raw_input()
            if (msg == 'exit'): 
                break
            data = self.sock.send(msg)
            time.sleep(0.001)
            print (data)



thr1 = MyThreadSend('send')
thr2 = MyThreadListen('listen')
thr1.start()
thr2.start()


    
