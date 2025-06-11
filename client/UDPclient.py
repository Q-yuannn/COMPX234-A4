import socket
import sys
def main():
    if len(sys.argv) != 4:
       print("The command you input is invalid!")
       sys.exit(1)
    # extract the arguments    
    hostname = sys.argv[0]
    portname = sys.argv[1]
    filename = sys.argv[2]
    # try to open files
    