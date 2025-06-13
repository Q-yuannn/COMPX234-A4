
import sys
import socket
import threading
import os
import random
import base64

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
        
        # create new socket and bind it to the new port
        data_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        data_socket.bind((hostname, data_port))
        
        # send OK message
        server_socket.sendto(ok_msg.encode(), client_address)
        
        # Open the requested file
        with open(filename, "rb") as f:
            while True:
                # receive the requested data
                request_data, address = data_socket.recvfrom(3072)
                request = request_data.decode().strip()
                request_parts = request.split()
                # invalid
                if request_parts[1] != filename:
                    continue
                # if request is close
                if len(request_parts) >= 3 and request_parts[2] == "CLOSE":
                    close_msg = f"FILE {filename} CLOSE_OK"
                    # use new socket to send close message to client
                    data_socket.sendto(close_msg.encode(), address)
                    break
                # if request is to get data in specfied file
                if request_parts[2] == "GET":
                    # get the start point and end point
                    start = int(request_parts[4])
                    end = int(request_parts[6])
                    length = end - start + 1
                    f.seek(start)
                    block = f.read(length)
                    # encode data 
                    encoded = base64.b64encode(block).decode()
                    # send the response message to client
                    response = f"FILE {filename} OK START {start} END {end} DATA {encoded}"
                    data_socket.sendto(response.encode(), address)
        data_socket.close()
        print(f"handle client requests finished")

    except Exception as e:
        print(f"Error: {e}")



def main():
     if len(sys.argv) != 2:
        print("Please input valid command")
        return
     print("Server is starting...")
     # if the command is valid
     port = int(sys.argv[1])
     # UDP socket
     server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     hostname = 'localhost'
     # bind host and port
     server_socket.bind((hostname, port))
     print(f"Server is running on {hostname}:{port}")
     while True:
           # receive request from client
           request, client_address = server_socket.recvfrom(3072)
           request_parts = request.decode().strip().split()
           # if the request is valid
           if len(request_parts) == 2 and request_parts[0] == "DOWNLOAD":
              # extract the file name from request
              file_name = request_parts[1]
              # create a new thread to handle the client request
              threading.Thread(target=handle_client_request, args=(file_name, client_address, server_socket,hostname)).start()
           else:
              print(f"Invalid request from {client_address}")

if __name__ == "__main__":
    main()
       

