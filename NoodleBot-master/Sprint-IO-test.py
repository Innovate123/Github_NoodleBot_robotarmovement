# Echo client program
import socket
import time
HOST = '192.168.0.100' # The remote host
PORT = 30000           # The same port as used by the server

print ("Starting Program")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ("Connected by", addr)
while 1:
    data = conn.recv(1024)
    print (data)
    if not data: break
    conn.send("(1,1,1)")
    print ("Last order completed...")
conn.close()