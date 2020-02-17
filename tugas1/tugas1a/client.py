import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
port = 31001
server_address = ('localhost', port)
print(f"connecting to {server_address}")
sock.connect(server_address)
try:
    # Send data
    fl = open("send.txt", 'rb')
    isi = fl.read(100)
    message = isi
    fl.close()
    print(f"sending {message}")
    sock.sendall(message)
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(64)
        amount_received += len(data)
        print(f"{ data.decode('utf-8') }")
finally:
    print("closing")
    sock.close()