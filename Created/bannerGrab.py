#!/usr/bin/python3

import socket

def banner(ip, port):
    s = socket.socket()
    s.settimeout(5)

    s.connect((ip, port))
    print(s.recv(1024))

def main():
    ip = input("Input the IP: ")
    port = int(input("Enter the port: "))
    banner(ip, port)

main()
