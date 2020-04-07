import socket
import sys
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 7777)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)
requestfile = "cegah.jpg"
request = (b"download "+requestfile.encode())
print("Mendownload file "+request.decode()+"...")
f = open(requestfile,"wb")
file =(b"")
sock.send(request)
data = sock.recv(1024)

while True:
    file = file + data
    print(data)

    if sys.getsizeof(data) != 1057:
        break

    else :
        data = sock.recv(1024)

file = base64.b64decode(file)
f.write(file)
f.close()

print("file "+requestfile+" berhasil didownload")
sock.close()
