filename = "send.txt"
f = open(filename,'rb')
l = f.read(100)
while(l):
    print(repr(l))
    l = f.read(100)
f.close()