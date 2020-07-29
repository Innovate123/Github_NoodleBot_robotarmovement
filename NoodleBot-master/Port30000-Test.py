# Echo client program
import socket
import time
HOST = "192.168.0.100" # The remote host
PORT = 30000           # The same port as used by the server
print ("Starting Program")
count = 0
 
while (count < 1000):
 print ("A")
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 print ("B")
 s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 print ("C")
 s.bind((HOST, PORT)) # Bind to the port 
 print ("D")
 s.listen(5) # Now wait for client connection.
 print ("E")
 conn, addr = s.accept() # Establish connection with client.
 print ("F")
try:
 msg = c.recv(1024)
 print ("msg")
 time.sleep(1)
 if msg == "asking_for_data":
  count = count + 1
  print ("The count is:", count)
  time.sleep(0.5)
  print ("")
  time.sleep(0.5)
  conn.send("(1)");
  print ("Sent var")
except socket.error as socketerror:
 print (count)
 
 c.close()
 s.close()
 print ("Program finish")