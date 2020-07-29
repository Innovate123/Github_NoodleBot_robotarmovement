# Echo client program
import socket
import time
HOST = "192.168.1.50"      # The remote host
PORT = 30001               # The same port as used by the server

print ("Starting Program")
s = socket.socket()         # Create a socket object
count = 0
count_2 = 0
data = 0
#s.bind((HOST, PORT))        # Bind to the port
#s.listen(5)                 # Now wait for client connection.
#c, addr = s.accept()        # Establish connection with client.
   
while (count < 1):

    count = count + 1
    print ("The count is:", count)
    time.sleep(0.5)
    print ("")
    msg = c.recv(1024)
    print ("The robot position is(XYZ vector)")
    print (msg)
    print ("")
    time.sleep(0.5)
    msg = c.recv(1024)
    print ("The robot position is(Joint angle)")
    print (msg)

    while (count_2 < 3):
        count_2 = count_2 + 1
        print ("")
        msg = c.recv(1024)
        print (msg)
        time.sleep(1)
        if msg == "Asking_Waypoint_1":
            c.send("(0.1,0.4,0.4,0.01,3.14,0.01)");
        if msg == "Asking_Waypoint_2":
            c.send("(0.1,0.4,0.3,0.01,3.14,0.01)");
        if msg == "Asking_Waypoint_3":
            c.send("(0.1,0.4,0.2,0.01,3.14,0.01)");
    print ("")
    msg = c.recv(1024)
    print ("The robot position is(XYZ vector)")
    print (msg)
    print ("")
    msg = c.recv(1024)
    print ("The robot position is(Joint angle)")
    print (msg)

c.close()

print ("Program finish")