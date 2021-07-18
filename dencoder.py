#!/usr/bin/python3
# Script: dencoder.py 
# Author : Opeyemi Atoyebi
# Twitter: @zidelnet 
# Program: SheHacks 2021
# Description: A basic script to encode and decode string in base64 within a specific iteration.  

# import base64 module 
import base64

# import sys module 
import sys 

# function to perform base64 encoding 
def base64_encoder(string): 
    return base64.b64encode(string.encode()).decode() 

# function to perform base64 decoding 
def base64_decoder(string): 
    return base64.b64decode(string.encode()).decode() 

print("[+] A simple script to encode and decode string in base64")

while True:
    try:  
        user_option = int(input("\n1: Encode base64\n2: Decode base64\n3: Exit program\n"))
        if user_option == 1: 
            print("\n[+] Base64 Encoder")
            user_str = input("Enter any string for base64 encoding: ")
            iteration = int(input("Enter the number of iteration\n"))
            
            for i in range(1,iteration+1): 
                user_str = base64_encoder(user_str)
                print("{} iteration is {}".format(i, user_str))
            
        elif user_option == 2: 
            print("\n[+] Base64 Decoder")
            user_str = input("Enter any base64 string for decoding: ")
            iteration = int(input("Enter the number of iteration\n")) 
            
            for i in range(1,iteration+1): 
                user_str = base64_decoder(user_str)
                print("{} iteration is {}".format(i, user_str))
        
        elif user_option == 3: 
            print("\n[+] Goodbye ...\n") 
            sys.exit(0)
        
        else: 
            print("\n[*] Invalid option, check your input\n")
        
    except ValueError as err: 
        print("\n[*] Option is not part of the program's option\n")
    
    
    