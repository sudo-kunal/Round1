#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#define the IP address of the server for connection purposes.
host = socket.gethostname()

port = 444

#Use the IP of server to connect to.
clientsocket.connect((host, port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))
