import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('which device:')
    if msg == 'quit':
        break
    
    s.send(msg.encode())

s.close()