import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
port = 31002
server_address = ('localhost', port)
print(f"connecting to {server_address}")
sock.connect(server_address)
with open('received.txt', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data...')
        data = sock.recv(100)
        print( data.decode('utf-8') )
        if not data:
            break
        # write data to a file
        f.write(data)
sock.close()