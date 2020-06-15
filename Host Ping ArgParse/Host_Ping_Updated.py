##############################################################################################

# This is a Basic Python Script for Ping Test

# User to input the Host IP and optional Ping Count and Timeout parameters

# Check ICMP rechability

# Should work in different OS (Windows / Linux / MacOS)

#Expected Result: up / down

##############################################################################################

import subprocess
import argparse
import sys
from subprocess import Popen, PIPE, call
from sys import platform
import os

# create main function
def main():

# create ArgumentParser object
    parser = argparse.ArgumentParser(description='Host Ping Script',\
     formatter_class=argparse.RawTextHelpFormatter)

# add arguments
    parser.add_argument("-c", "--c" , help="\tNumber of Packets", action="store"\
        , type=int, choices=range(1, 26), metavar=("(1-25)"), default=5)
    parser.add_argument("-w", "--w" , help="\tTimeout in Seconds", action="store"\
        , type=int, choices=range(1, 26), metavar=("(1-25)"), default=5)
    parser.add_argument("-ip", "--ip", help="\tIP Address", action="store"\
        , required=True)

# parse command-line arguments
    args = parser.parse_args()

# Identification of Device OS and Ping CLI execution!

    if platform == 'linux' or platform == 'linux2':
        print('\n\nYour Device Platform is Linux')
        output = subprocess.check_output("ping -c {} {}".format(args.c, args.ip), shell=True, universal_newlines=True)
        print(output)
    elif platform == 'darwin':
        print('\n\nYour Device Platform is MacOS\n\n')
        output = subprocess.check_output("ping -c {} {}".format(args.c, args.ip), shell=True, universal_newlines=True)
        print(output)
    elif platform == "win32": 
        print('\n\nYour Device Platform is Windows')
        output = subprocess.check_output("ping -c {} {}".format(args.c, args.ip), shell=True, universal_newlines=True)
        print(output)


if __name__ == "__main__" and len(sys.argv) < 2:
    print ("use the -h flag for help on this script")
else:
    main()
