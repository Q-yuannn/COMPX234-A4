import sys
import socket
import threading




def main():
     if len(sys.argv) != 2:
        print("Please input valid command")
        return
     # if the command is valid
     port = int(sys.argv[1])
     # UDP socket
     server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     hostname = "WangQiyuan"
     # bind host and port
     server_socket.bind((hostname, port))
     while True:
           request, client_address = server_socket.recvfrom(1024)
           request_parts = request.decode().strip().split()

           if len(request_parts) == 2 and request_parts[0] == "DOWNLOAD":
              filename = request_parts[1]
              threading.Thread(target=handle_client, args=(filename, client_address, server_socket)).start()
           else:
              print(f"Invalid request from {client_address}")
       

