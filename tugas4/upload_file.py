import socket
import sys
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 7777)
print(sys.stderr, 'connecting to %s port %s' % server_address)

sock.connect(server_address)
pesan = ("upload cucitangan.jpg")
namafile = "".join(pesan.split() [1])
f = open(namafile, "rb")
panjang = len(namafile)+1
isifile = base64.encodestring(f.read())
f.close()

f = open("base64encode","wb")
f.write(isifile)
f.close()

f = open("base64encode","rb")
l = pesan.encode()+(b" ")+f.read(1024)
print(l)

while (l):
    sock.send(l)
    l =f.read(1024)
    data = sock.recv(1024)
print(data)

sock.close()