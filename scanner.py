#!/bin/python3

#basic simple port scanner without threading

import sys

import socket 
from datetime import datetime as dt


#define our target 

if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])

else: 
	print("Invalid amount of arguments.")
	print("Use proper syntax: python3 scanner.py <ip>")
	sys.exit()

print("-" * 50)
print("Hostname of machine: " + socket.gethostname())
print("Scanning target " + target)
print("FQDN of target: " + socket.getfqdn(target))
print("Time started: " + str(dt.now()))
print("-" * 50)

try: 
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #is a float
		result = s.connect_ex((target,port)) #returns error indicator
		print("Checking port {}".format(port))
		
		if result == 0:
			print("Port {} is open".format(port))
			
		s.close()
		
except KeyboardInterrupt:
	print("\nExiting program...")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print ("Couldn't connect to server.")
	sys.exit()
	
