# COMPX234-A4
System and Network Assignment4

This project implements a reliable file transfer system over UDP, consisting of a **server (UDPserver.py)** and a **client (UDPclient.py)**. It supports file requests, chunked transmission, retransmissions, and proper connection closure, allowing multiple files to be downloaded 

sequentially.
## Project Structure
├── server

│ └── UDPserver.py # UDP file server

│ └── test1.png

│ └── test2.pptx

│ └── test.txt

├── client

│ └── UDPclient.py # UDP file client

│ └──filename_list.txt # List of filenames to download (client input)

└── README.md # Project description

## Features

- **Server**:
  - Listens for client requests to download files
  - Responds with file size and a data transfer port
  - Handles chunked file data transfer with retransmission support
  - Manages file transmission closure commands

- **Client**:
  - Reads a list of filenames and requests each file from the server
  - Downloads files in chunks and writes them sequentially to disk
  - Displays a progress bar (stars or percentage) for file downloads
  - Sends a close request after finishing each file transfer

## Run
### 1. Start the server

Navigate to the `server` directory and run:

python UDPserver.py <port>

### 2. Run the client
Navigate to the client directory and run:
python UDPclient.py <server_IP> <server_port> <filename_list>

## Notes
The system uses UDP and implements basic retransmission to improve reliability.

Large files are transferred in chunks limited by buffer sizes.

Test on a local or LAN environment for best results.

Server and client must use the matching protocol format.

## Example Output

Downloading test1.png: 100% [977633/977633 bytes]:test1.png transmission completed

Downloading test2.pptx: 100% [22890377/22890377 bytes]:test2.pptx transmission completed

Downloading test3.txt: 100% [23/23 bytes]:test3.txt transmission complete
