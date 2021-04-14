import socket
from random import randint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3333))
s.listen(10)

heart = randint(40, 140)
walk = randint(2000, 6000)
kal = randint(1000, 4000)

while True:
    client, addr = s.accept()
    data = client.recv(1024)
    msg = data.decode()
    if(msg == '2'):
        
    
    else:
        break