#!/usr/bin/env python
# coding: utf-8

# This is a Basic Python Script for Ping Test which will not use any new Python Libraries

# User to input the Host IP and Ping Count

# Check ICMP rechability

# Should work in different OS (Windows / Linux / MacOS)

#Expected Result: up / down


##############################################################################################

from sys import platform
import os

# Request User for inputing Host IP Address whose reachability needs to be verified

host_ip = input('Enter Host IP for Ping Test:  ')

print('\n')

# Request User for number of packets to be sent to the Host for Ping test

ping_count = input('Enter Count for Ping Test:  ')

print('\n')

# Check the User's Device Platform and execute the appropriate Ping CLI with Count keyword
# Followed by printing the Ping result

if platform == 'linux' or platform == 'linux2':
    print('Your Device Platform is Linux')
    response = os.system("ping " + host_ip + " -c " + ping_count)
    
    if response == 0:
        print ("Host " + host_ip + " is up")
    else:
        print ("Host " + host_ip + " is down")

elif platform == 'darwin':
    print('Your Device Platform is MacOS\n\n')
    response = os.system("ping " + host_ip + " -c " + ping_count)
    
    if response == 0:
        print ("Host " + host_ip + " is up")
    else:
        print ("Host " + host_ip + " is down")

elif platform == "win32":
    print('Your Device Platform is Windows')
    response = os.system("ping " + host_ip + " -n " + ping_count)
    
    if response == 0:
        print ("Host " + host_ip + " is up")
    else:
        print ("Host " + host_ip + " is down")

elif platform != 'linux' or platform != 'linux2' or platform != 'darwin' or platform != 'win32':
    print('Unknown Device Platform. Contact Administrator!')

    
# End of Script




