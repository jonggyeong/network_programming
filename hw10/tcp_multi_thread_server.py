from socket import *   
import threading
import time 

port = 3333
BUFFSIZE = 1024
clients = []  

s = socket(AF_INET, SOCK_DGRAM)  
s.bind(('',port))

print('Server Started')

while True:  
    data, addr = s.recvfrom(BUFFSIZE)
    if 'quit' in data.decode():  
        if addr in clients:  
            print(addr, 'exited')  
            clients.remove(addr)  
            continue
        
    if addr not in clients:  
        print('newclient', addr)  
        clients.append(addr)  
        
    print(time.asctime() + str(addr) + ':' + data.decode())  
    
    for client in clients:  
        if client != addr:  
            s.sendto(data, client)