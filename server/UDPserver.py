import sys
import socket
import threading
import os
import random

def handle_client_request(filename, client_address, server_socket, hostname):
    try:
        # trt to get the file
        # if getting fail, send fail mesaage
        if not os.path.exists(filename):
            err_msg = f"ERR {filename} NOT_FOUND"
            server_socket.sendto(err_msg.encode(), client_address)
            return
        # if file exists, send OK message,file size, and port number
        filesize = os.path.getsize(filename)
        # randomly select port number
        data_port = random.randint(50000,51000)
        ok_msg = f"OK {filename} SIZE {filesize} PORT {data_port}"
        
        
        # send OK message
        server_socket.sendto(ok_msg.encode(), client_address)


    except Exception as e:
        print(f"Error: {e}")



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
              file_name = request_parts[1]
              threading.Thread(target=handle_client_request, args=(file_name, client_address, server_socket)).start()
           else:
              print(f"Invalid request from {client_address}")
       

