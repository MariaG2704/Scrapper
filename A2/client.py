import socket
import sys
import threading

def listen_to_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('ascii')
            if message == "/quit" or not message: 
                print("Disconnected")
                break
            print(f'{message}')
            print("Reply in line below or type /quit to quit")
        except Exception as e:
            print(f'Error recieving message: {e}')
            break

def send_message(message,client_socket):
        try:
            client_socket.send(message.encode('ascii'))
        except Exception as e:
            print(f'Error sending message: {e}')

def main():
    if len(sys.argv)!=3:
        print("Input is wrong, type: python3 client.py <host> <port>")
    else:
        host=str(sys.argv[1])
        port= int(sys.argv[2])
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        except socket.error as err: 
            print ("Socket creation failed with error %s" %(err))

        try:
            client_socket.connect((host,port))
            print(f'The socket has been successfully connected to the server')
        except socket.error as err:
            print(f'Socket failed to connect to server with errror')
            print(f'Please check port and host and try again')
        recieved_message = threading.Thread(target=listen_to_message, args=(client_socket, ))
        recieved_message.start()
        while True:
            print(f'Type /quit to leave chat or type your message on the line below')
            message = input()
            new_thread= threading.Thread(target = send_message,args=(message, client_socket,))
            new_thread.start()
            if message == "/quit" or not message:
                print("You have left")
                break     
        client_socket.close() 
        
    

if __name__=="__main__":
    main() 
