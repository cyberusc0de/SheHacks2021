#!/usr/bin/python3
# Script: inforecon.py 
# Author : Opeyemi Atoyebi
# Twitter: @zidelnet 
# Program: SheHacks 2021
# Description: A basic script to perform reconnaisance on any website 

# import necessary modules required  
import sys 
import requests 
import socket
import json 

if len(sys.argv) < 2: 
    print("Usage: " + sys.argv[0] + " <domain_name>")
    sys.exit(0)

print("Information Gathering on " + sys.argv[1] + " in progress ...")
print("[+]================================================\n")

# get the IP Address of target 
getip = socket.gethostbyname(sys.argv[1])

#ipinfo.io API
req = requests.get("https://ipinfo.io/" + getip + "/json")
respond = json.loads(req.text)

print("IP:        \t" + respond['ip'])
print("Location:  \t" + respond["loc"]) 
print("Region:    \t" + respond["region"])
print("City:      \t" + respond["city"]) 
print("Country:   \t" + respond["country"])
#print("hostname:  \t" + respond["hostname"])
#print("Timezone:  \t" + respond["timezone\n"])    
    