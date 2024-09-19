import socket
import sys
from _thread import *
import threading

# opens output file and writes my HawkId and name 
file = open('/home/mgauna/cs3640/A2/output.txt','w+')
file.write('msgauna Maria Gauna \n') 
file.write('\n')
file.flush()

#creates a set 
set_of_clients = set()

 
def client_thread(conn):
    # adds a connection to a set.
    set_of_clients.add(conn)
    conn_name = conn.getpeername()[1]

    # This thread then ends a loop waiting for messages from the connection and decodes it 
    # Following instructions on how to quit ( removes that client from the set)
    # Sends the connections message to all the clients in the set
    # And prints on communications to output file and console
    while True: 
        data = conn.recv(1024).decode('ascii')
        if not data or data == '/quit':
            print(f'Goodbye. User [{conn_name}] has left chat')
            file.write(f'\nUser [{conn_name}] has left the chat\n')
            file.flush()
            set_of_clients.remove(conn)
            break
        else:
            message_recv= f'\nUser [{conn_name}]: {data}'
            print(message_recv)
            file.write(f'\n User [{conn_name}] sent: [{data}]\n')
            file.flush
            for c in set_of_clients:
                if c != conn:
                    c_name= c.getpeername()[1]
                    file.write(f'\nUser [{c_name}] recieved message: [{data}] from User [{conn_name}]\n')
                    file.flush()
                    c.send(message_recv.encode("ascii"))
                    
            file.write(f'\n')
            file.flush()
    conn.close()

# Main that creates a socket from input in command line
# Binds that socket to a host and port, and the listens on that port 
# while accepting new clients and creates a new thread for each client
# All while printing communications to an output file and the console
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if len(sys.argv)==2:
        port= int(sys.argv[1])
        try:
            host= socket.gethostbyname("127.0.0.1")
        except socket.gaierror: 
            print("there was an error in resolving the host")
            sys.exit()
         
        server_socket.bind((host,port))
        print(f'The socket has connected to {port}')
        file.write(f'\nThe server has been created and connected to {port}\n')
        file.flush()
        server_socket.listen(6) 
        print(f'{host} is listening on port: {port}') 
        file.write(f'\nThe server is now listening.\n')
        file.flush()

        while True:
            client,address = server_socket.accept()
            file.write(f'\nUser [{address[1]}] has joined\n')
            file.flush()
            print(f'User [{address[1]}] has joined ')
            client = threading.Thread(target= client_thread ,args=(client, ))
            client.start()
    server_socket.close()      

#calls the main function
if __name__=="__main__":
    main()  
# closes the file
file.close()