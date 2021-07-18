#!/usr/bin/python3
# Script: pscanner.py 
# Author : Opeyemi Atoyebi
# Twitter: @zidelnet 
# Program: SheHacks 2021
# Description: Building a basic port scanner using nmap in python  
# target: 45.33.32.156 (scanme.nmap.org)

try: 
    # import nmap module 
    import nmap 

    #import sys module 
    import sys 

    if len(sys.argv) > 2: 
        print("[*] Invalid command!!\n[+] Option 1: python3 pscanner.py <target>\n[+] Option 2: ./pscanner.py <target>\n[+] Example: python3 pscanner.py 45.33.32.156\n")
        sys.exit(0)
        
    # parsing the target to the argument 0 
    target = str(sys.argv[1]) 
    
    # Declaring ports to be scan 
    ports = [80,443]

    # Declaring the PortScanner instance 
    scan_v = nmap.PortScanner() 

    # print what the program is doing 
    print("\n[+] Scanning ", target, " for port 80, 443 ...\n")

    # Looping through the ports for scanning 
    for port in ports: 
        portscan = scan_v.scan(target, str(port)) 
        print("Port",port," is ",portscan['scan'][list(portscan['scan'])[0]]['tcp'][port]['state'])

    print("\nHost",target," is ",portscan['scan'][list(portscan['scan'])[0]]['tcp'][port]['state'])
    print("[+] Scanning Completed ...")
    
except ModuleNotFoundError: 
    print("Nmap not found ! kindly install nmap and python module")
    print("pip install python-nmap")
