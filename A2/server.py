import socket
import sys
from _thread import *
import threading

file = open('/home/mgauna/cs3640/A2/output.txt','w+')
file.write('msgauna Maria Gauna \n') 
file.write('\n')
file.flush()
set_of_clients = set()

def client_thread(conn):
    set_of_clients.add(conn)
    conn_name = conn.getpeername()[1]

    while True: 
        data = conn.recv(1024).decode('ascii')
        if not data or data == '/quit':
            print(f'Goodbye. User [{conn_name}] has left chat')
            file.write(f'\nUser [{conn_name}] has left the chat \n')
            file.flush()
            set_of_clients.remove(conn)
            break
        else:
            message_recv= f'User [{conn_name}]: {data}'
            file.write(message_recv)
            file.flush()
            print(message_recv)
            file.write(f'\n User [{conn_name}] sent [{data}]')
            file.flush
            for c in set_of_clients:
                if c != conn:
                    c_name= c.getpeername()[1]
                    file.write(f'\n User [{c_name}] recieved [{data}] from User [{conn_name}]')
                    file.flush()
                    c.send(message_recv.encode("ascii"))
                    
            file.write(f'\n')
            file.flush()
    conn.close()


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(sys.argv)==2:
        port= int(sys.argv[1])
        host= socket.gethostbyname("127.0.0.1")
         
        server_socket.bind((host,port))
        print(f'The socket has connected to {port}')
        server_socket.listen(6) 
        print(f'{host} is listening on port: {port}') 

        while True:
            client,address = server_socket.accept()
            file.write(f' \n User [{address[1]}] has joined \n')
            file.flush()
            print(f' User [{address[1]}] has joined ')
            client = threading.Thread(target= client_thread ,args=(client, ))
            client.start()
    server_socket.close()      

        
if __name__=="__main__":
    main()  

file.close()