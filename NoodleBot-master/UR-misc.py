# Echo client program
import socket
import time
HOST = "192.168.1.50"    # The remote host
PORT = 30002             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
time.sleep(2)
print ("okok")
s.send ("movej([-0.5, -2.3, -1.3, -2.2, 3.3, -1.2], a=1.4, v=1.05)" + "\n")
s.send ("servoj(get_inverse_kin(p [-0.028682, -0.467049, 0.0500, -3.14159, 0, 0], t=0.05)")
print ("okok")
# s.send ("movej([-0.5405182705025187, -2.350330184112267, -1.316631037266588, -2.2775736604458237, 3.3528323423665642, -1.2291967454894914], a=1.3962634015954636, v=1.0471975511965976)" + "\n")
# s.send ("set_digital_out(4,False)" + "\n")
data = s.recv(1024)
s.close()
print ("Received", repr(data))