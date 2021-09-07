#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Created a socket object that used socket function to define socket family and socket type.

host = socket.gethostname()
#value given to the host
#can use custom static values too. But this function is better when you are running server on windows.

port = 444
# value given to the port
# port value under 1024 will give an error when run in an underprevileged mode... must use sudo

serversocket.bind((host, port))
# used the server socket object and binded it to the host and port
 
serversocket.listen(3)
# Set up a tcp listener to listen to upto 3 tcp connections


while(True):
    clientsocket, address = serversocket.accept()
    #accept the connection

    print("recieved connection from " % str(address))
    #shows on the server

    message = "hello! thanks for connecting to the server" + "\r\n"
    #created the message to be sent to the client

    clientsocket.send(message.encode('ascii'))
    #send message to the client
    clientsocket.close()
    
