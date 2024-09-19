import socket
import sys
import threading

def listen_to_message(client_socket):
    # function that loops continuosly until an exception occurs or (/quit) is typed,
    # listening to messages from a server, prints out the message 
    # and prompts user for a response
    while True:
        try:
            message = client_socket.recv(1024).decode('ascii')
            if message == "/quit" or not message: 
                break
            print(f'{message}')
            print("Reply in line below or type /quit to quit")
        except Exception as e:
            print(f'Error recieving message: {e}')
            break

# sends a message to a client_socket
def send_message(message,client_socket):
    client_socket.send(message.encode('ascii'))

def main():
    # Main that creates a new client_socket based on the command line input
    if len(sys.argv)!=3:
            print("Input is wrong, type: python3 client.py <host> <port>")
    else:
        host=str(sys.argv[1])
        port= int(sys.argv[2])
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        except socket.error as err: 
            print ("Socket creation failed with error %s" %(err))
        
        #connects that client to the server 
        try:
            client_socket.connect((host,port))
            print(f'The socket has been successfully connected to the server')
                
        except socket.error as err:
            print(f'Failed to connect to server with errror')
            print(f'Please check port and host and try again')
            sys.exit()
         
        # thread used to listen for messages from the server
        recieved_message = threading.Thread(target=listen_to_message, args=(client_socket, ))
        recieved_message.start()
         
        # loop that continuously prompts the user for an input 
        # and then sends that input the server
        while True:
            print(f'Type /quit to leave chat or type your message on the line below')
            message = input()
            new_thread= threading.Thread(target = send_message,args=(message, client_socket,))
            new_thread.start()
            if message == "/quit" or not message:
                break     
        client_socket.close() 
        
    

if __name__=="__main__":
    main() 
