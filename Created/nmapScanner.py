#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print('Welcome to the nmap scanner python tool!!!')
print('------------------------------------------')

ip_addr = input("Please enter the IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr) #Sanitisation of the input

#response of the user for the scan type
resp = input("""\n Please enter the type of scan you want to run... 
                    1)SYN AC Scan
                    2)UDP Scan
                    3)Comprehensive scan \n>""")

print("You have selected the option: ", resp)

if resp == '1': #TCP scan
    print("NMAP version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS')# scanning process
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())# whether the target is up or down
    print(scanner[ip_addr].all_protocols())#all the protocols would be printed by this
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':#UDP scan
    print("NMAP version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sU')# scanning process
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())# whether the target is up or down
    print(scanner[ip_addr].all_protocols())#all the protocols would be printed by this
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())    
elif resp == '3':
    print("NMAP version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O')# scanning process
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())# whether the target is up or down
    print(scanner[ip_addr].all_protocols())#all the protocols would be printed by this
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp >= '4':
    print("Please enter a valid option!!!")

