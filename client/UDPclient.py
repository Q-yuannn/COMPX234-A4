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
    # try to open namelist file
    # the namelist file is in the last folder
    with open(f'../{filename}.txt', 'r') as file:
         # create datagram socket(UDP)
         datagram_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
