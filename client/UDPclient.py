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
        for line in file:
            file_name = line.strip()
            download_message = f"DOWNLOAD <{file_name}>"
            download_mes_packet = download_message.encode()
