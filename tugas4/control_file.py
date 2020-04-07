import shelve
import uuid
import socket
import os
import base64

class Direct:
    def __init__(self):
        if not os.path.exists("file"):
            os.makedirs("file")
    def upload_file(self,nama=None,file=None):
       # check file name
        data_file = file
        print(base64.decodestring(data_file))
        f = open("file/"+nama,"wb")
        f.write(base64.decodestring(data_file))
        return True

    def download_file(self,nama=None):
        # read file
        are = []
        f = open("file/" + nama, "rb")
        l =f.read()
        f.close()
        print(l)

        # download
        hasil = base64.encodestring(l)
        print(hasil)
        are.append(hasil.decode())
        print(are)
        return are

    def list_file(self):
        file_list = os.listdir("file")
        f = []
        for filename in file_list:
            f.append(filename)
        return f

if __name__=='__main__':
    direct = Direct()
    input = "pesan.txt"
    print(direct.list_file())
