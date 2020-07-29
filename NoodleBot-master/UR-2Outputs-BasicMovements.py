# Echo client program
import socket
import time
HOST = "192.168.1.50"    # The remote host
PORT = 30002             # The same port as used by the server
print ("Starting Program")
count = 0
while (count < 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    time.sleep(0.05)


    time.sleep(3)
    #s.send ("RG2(86,40,0.0,True,False,False)")
    #time.sleep(1)
    s.send ("movej(get_inverse_kin(p[.092938561274, -.353096816926, .462595264904, 1.169187776176, -1.240793336641, 1.170914400796], qnear=[1.5453579425811768, -2.3914130369769495, 2.4199042320251465, 3.116952419281006, 4.683440208435059, 1.570770502090454]), a=1.3962634015954636, v=1.75)" + "\n")
    print ("At WP#1")
    time.sleep(2)
    s.send ("movej(get_inverse_kin(p[.281568217520, -.356493013793, .057061723406, 2.450866173885, -1.081220952716, -.397286041086], qnear=[2.2888543605804443, -1.4530819098102015, 2.0287861824035645, 4.22260046005249, 4.191213130950928, 1.5708423852920532]), a=1.3962634015954636, v=1.75)" + "\n")
    print ("At WP#2")
    time.sleep(2)
    #s.send ("RG2(0,40,0.0,True,False,False)")
    #time.sleep(1)
    s.send ("movej(get_inverse_kin(p[.275230298703, -.365243581076, .083857619998, 2.408240585724, -1.062846013313, -.407384482214], qnear=[2.2886676190590673, -1.4800466948712039, 1.9997310378334436, 4.2705543643810895, 4.145734757325876, 1.5710746059430618]), a=1.3962634015954636, v=1.75)" + "\n")
    print ("At WP#3")
    time.sleep(2)
    s.send ("movej(get_inverse_kin(p[-.110350396857, -.365263356202, .083888695031, 2.408261056423, -1.062717481186, -.407365573496], qnear=[1.207298279928704, -1.9197418876288914, 2.5219256390605835, 3.629351954888161, 4.395765421676284, 0.38592967372434117]), a=1.3962634015954636, v=1.75)" + "\n")
    print ("At WP#4")
    time.sleep(2)
    s.send ("movej(get_inverse_kin(p[-.113250855454, -.352969852840, .056401326375, 2.474276899734, -1.083328779750, -.456908114775], qnear=[1.2068231105804443, -1.8675296942340296, 2.5386509895324707, 3.6364006996154785, 4.3687286376953125, 0.3865043818950653]), a=1.3962634015954636, v=1.75)" + "\n")
    print ("At WP#5")
    time.sleep(2)
    
    s.send ("set_digital_out(4,True)" + "\n")
    time.sleep(0.5)
    s.send ("set_digital_out(5,True)" + "\n")
    time.sleep(1)    
    
    #s.send ("RG2(70,40,0.0,True,False,False)")
    #time.sleep(1)

    s.send ("set_digital_out(4,False)" + "\n")
    time.sleep(0.5)
    s.send ("set_digital_out(5,False)" + "\n")
    time.sleep(1)

count = count + 1
print ("The count is:", count)
print ("Program finish")
time.sleep(1)
data = s.recv(1024)
s.close()
print ("Received", repr(data))
print ("Status data received from robot")