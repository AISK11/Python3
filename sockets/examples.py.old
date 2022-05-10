import threading
import socket

nickname= input("Choose a nickname:")

PORT = 9999
#SERVER = '10.131.66.225'
SERVER = '10.46.76.24'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER,PORT))

def recieve():
    while True:
        try:
            message = client.recv(1024).decode('ascii') #message from server
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=recieve)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

###########################################

import threading
import socket

#host = '127.0.0.1' #localhost
host = socket.gethostbyname(socket.gethostname())

print(host)
port = 9999

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break


def recieve():
    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}")


        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}!")
        broadcast(f'{nickname} joined the chat!'.encode('ascii'))
        client.send('Connected to the server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args =(client,))
        thread.start()

print("Server is listening...")
recieve()
