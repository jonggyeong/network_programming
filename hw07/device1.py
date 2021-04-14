import socket
from random import randint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3333))
s.listen(10)

temp = randint(0, 40)
humi = randint(0, 100)
light = randint(70, 150)

while True:
    client, addr = s.accept()
    data = client.recv(1024)
    msg = data.decode()
    if(msg == '1'):
        
        
    else:
        break
    
