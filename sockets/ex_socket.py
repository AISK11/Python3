#!/usr/bin/env python3

################################################################################
##                                   README                                   ##
################################################################################
## Demo example how to use sockets in Python3.

################################################################################
##                                  Theory                                    ##
################################################################################
'''
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
'''


################################################################################
##                                  Modules                                   ##
################################################################################
## Docs: https://docs.python.org/3/library/socket.html
import socket


################################################################################
##                                 Functions                                  ##
################################################################################
## Program starting function.
def main():
    pass


## Python3 program start execution.
if __name__ == "__main__":
    main()
