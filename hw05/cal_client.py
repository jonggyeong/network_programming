import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 3333))

while True:
    msg = input('Calculator to send:')
    if msg == 'q':
        break
    
    s.send(msg.encode())

    print('Calculate message:', s.recv(1024).decode())

s.close()