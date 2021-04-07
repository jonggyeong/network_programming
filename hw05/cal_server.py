import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting..')

while True:
     client, addr = s.accept()
     print('connection from ', addr)
     while True:
        data = client.recv(1024)
        rsp = eval(data.decode())
        msg = str(rsp)
        client.send(msg.encode())
        client.close()