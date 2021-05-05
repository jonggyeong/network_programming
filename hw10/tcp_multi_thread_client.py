from socket import *
import threading

port = 3333
BUFFSIZE = 1024

def recvTask(sock):  
    while True:  
        data, addr = sock.recvfrom(BUFFSIZE)  
        print(data.decode())  
 
sock = socket(AF_INET,SOCK_DGRAM)  
svr_addr = ('localhost', port)

my_id = input('ID를 입력세요:')  
sock.sendto(('['+my_id+']').encode(), svr_addr)  

th = threading.Thread(target = recvTask, args=(sock,))  
th.daemon = True  
th.start()  

while True:  
    data = '['+my_id+']' + input()  
    sock.sendto(data.encode(), svr_addr)