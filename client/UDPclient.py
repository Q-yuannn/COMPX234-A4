import socket
import sys
import time
import os

def sendAndReceive(packet, socket, server_address):
    timeout = 100
    try_time = 0
    maxtry_time = 30
    while try_time < maxtry_time:
        try:
            socket.settimeout(timeout)
            # send message
            socket.sendto(packet, server_address)
            # receieve response
            response, server_address = socket.recvfrom(1024)
            print(f"{response} received from {server_address} ")
            return response.decode('utf-8')
        
        # if timeout
        except socket.timeout:
            try_time += 1
            print(f"Timeout!")
            timeout += timeout
            return None


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
        for line in file:
            file_name = line.strip()
            download_message = f"DOWNLOAD <{file_name}>"
            download_mes_packet = download_message.encode()
