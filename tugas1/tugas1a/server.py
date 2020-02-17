import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
port = 31001
server_address = ('localhost', port)
print("starting up")
print(f"connection from {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    with open('received.txt', 'wb') as fl:
        print("opened")
        while True:
            data = connection.recv(100)
            print(f"received { data.decode('utf-8') }")
            if data:
                fl.write(data)
                print("sending back data")
                connection.sendall(data)
            else:
                print("no more data")
                break
    fl.close()
    # Clean up the connection
    connection.close()