import socket
import sys
import time
import os
import base64

def sendAndReceive(packet, socket, server_address,port):
    timeout = 100
    try_time = 0
    maxtry_time = 30
    while try_time < maxtry_time:
        try:
            socket.settimeout(timeout)
            # send message
            socket.sendto(packet, (server_address,port))
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
    
    Max_message_size = 1000
    if len(sys.argv) != 4:
       print("The command you input is invalid!")
       sys.exit(1)
    # extract the arguments    
    hostname = sys.argv[0]
    portname = sys.argv[1]
    list_filename = sys.argv[2]
    # try to open namelist file
    # the namelist file is in the last folder
    with open(f'../{list_filename}.txt', 'r') as file:
         # create datagram socket(UDP)
         datagram_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         # open the file name list
         for line in file:
             file_name = line.strip()
             download_message = f"DOWNLOAD <{file_name}>"
             download_mes_packet = download_message.encode()
             # send download request and handle response
             response = sendAndReceive(download_mes_packet, datagram_socket, hostname, portname)
             if response == None:
                print(f"No response for {file_name}")
                return
             else :
                # divide the response
                response_parts = response.strip().split
                if response_parts[0] == "ERR":
                   print(f"The file{file_name} Not found")
                   return
                # if receive the: OK response OK <filename> SIZE <size_bytes> PORT <port_number>
                size_index = response_parts.index("SIZE")
                port_index = response_parts.index("PORT")
                file_size = int(response_parts[size_index + 1])
                data_port = int(response_parts[port_index + 1])
                
                # write file bytes part
                with open(file_name, 'wb') as f:
                     downloaded = 0
                     while downloaded < file_size:
                         end = min(downloaded + Max_message_size, file_size-1)
                         # send write bytes request and handle response
                         request_message = f"FILE {file_name} GET START {downloaded} END {end}"
                         write_response = sendAndReceive(datagram_socket, request_message, hostname,data_port)
                         if response == None:
                             print(f"Unsuccessfully receive data{downloaded} - {end}")
                             return
                         # when reponse is not None, check response
                         write_response_parts = write_response.split("DATA",1)
                         if len(write_response_parts) < 2:
                             print("Invalid data response")
                             return
                         # if response is valid
                         # write bytes to the flie
                         encoded_data = write_response_parts[1].strip()
                         data = base64.b64decode(encoded_data)
                         f.seek(downloaded)
                         f.write(data)
                         downloaded += len(data)
                         print("*", end="", flush=True)
                     # after writing, send close request to the server
                     close_request = f"FILE {file_name} CLOSE"
                     # handle response
                     response = sendAndReceive(datagram_socket, close_request, hostname, data_port)
                     if response == None or "CLOSE_OK" not in response:
                        print(f"No right response from {file_name}")
                     else:
                        print(f":{file_name} transmission completed")
         # after writing, close the socket
         datagram_socket.close()

if __name__ == "__main__":
    main()
                         
                         


                

                 
                 

                 
