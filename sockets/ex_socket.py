#!/usr/bin/env python3

################################################################################
##                                   README                                   ##
################################################################################
## Demo example how to use sockets in Python3.


################################################################################
##                                  Theory                                    ##
################################################################################
'''
Socket - combination of port and IP address.


      Server
    +--------+
    | socket |
    |   |    |
    |  bind  |
    |   |    |
    | listen |                         Client
    |   |    |                       +---------+
    | accept |                       | socket  |
    |   |    |                       |    |    |
    |   |    |<- 3-way handshake ----| connect |
    |   |    |                       |    |    |
+-->|  recv  |<- client send data ---|  send   |<--+
|   |   |    |                       |    |    |   |
+---|  send  |-- server send data -->|  recv   |---+
    |   |    |                       |    |    |
    |  recv  |<- client send close --|  close  |
    |   |    |                       +---------+
    | close  |
    +--------+


Additional resources:
- https://www.youtube.com/watch?v=3QiPPX-KeSc
- https://stackoverflow.com/questions/4465959/python-errno-98-address-already-in-use
'''


################################################################################
##                                  Modules                                   ##
################################################################################
## Docs: https://docs.python.org/3/library/socket.html
import socket
## Docs: https://docs.python.org/3/library/threading.html
import threading


################################################################################
##                             Public Variables                               ##
################################################################################
## Specify server IPv4 and Port to listen on.
L_HOST = "127.0.0.1"
L_PORT = 5555

## Buffer size of the sent message.
BUFSIZE = 64
## Format of the message.
FORMAT = "utf-8"

## Specify disconnect message.
DISCONNECT_MSG = "!disconnect"

################################################################################
##                                 Functions                                  ##
################################################################################

def handle_client(conn, addr):
    print(f"New connection from {addr[0]}:{addr[1]}. Current connections: {threading.active_count() - 1}")

    while True:
        msg_length = int(conn.recv(BUFSIZE).decode(FORMAT))
        if msg_length:
            msg = conn.recv(msg_length).decode(FORMAT)
            print(f"{msg}")
            if msg == DISCONNECT_MSG:
                break
    conn.close()


## Program starting function.
def main():
    ## Initialize socket as IPv4 TCP.
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ## Bind (L_HOST, L_PORT) to socket.
    server.bind((L_HOST, L_PORT))

    ## Start listening on a socket.
    server.listen()
    print(f"Listening on {L_HOST}:{L_PORT}")

    while True:
        ## Accept new connection.
        ## conn: <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 5555), raddr=('127.0.0.2', 35843)>
        ## addr: ('127.0.0.2', 35843)
        conn, addr = server.accept()

        ## Create thread for each accepted connection.
        t = threading.Thread(target=handle_client, args=(conn, addr,))
        t.start()


## Python3 program start execution.
if __name__ == "__main__":
    main()
