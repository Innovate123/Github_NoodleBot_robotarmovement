# Echo client program
import socket
HOST = "192.168.1.50"    # The remote host
PORT = 30002             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send("set_digital_out(2,True)", "\n")
# s.send("set_digital_out(2,False)" + "\n")
data = s.recv(1024)
s.close()
print ("Received", repr(data))
