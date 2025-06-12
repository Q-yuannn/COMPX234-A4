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
