#!/usr/bin/python3

#target site: hackthissite.org : 137.74.187.101:443
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Enter the IP address: ")
port = int(input("Enter the port You want to scan: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print("The connection is closed!")
    else:
        print("The port is open!!")

portScanner(port)

