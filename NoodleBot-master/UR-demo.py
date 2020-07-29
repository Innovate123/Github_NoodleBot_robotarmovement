import socket
import time
HOST = "192.168.1.50"  # The remote host
PORT = 30001           # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

#def instructionForTheRobot(movementList):
#    for msg in movementList:
#        print(msg[0])
#        s.send(msg[0].encode('utf-8'))
#        time.sleep(msg[1])

print("Start moving...")

cmd = "movej(get_inverse_kin(p[.310685954920, -.432811206531, .103701968061, 2.147440496121, -.860423547195, -.396913579725], qnear=[2.3123621940612793, -1.4278877417193812, 2.012190818786621, 4.051218509674072, 3.8497791290283203, -1.6746299902545374]), a=1.3962634015954636, v=1.0471975511965976)" + "/n"
s.send (cmd.encode('utf-8'))
time.sleep(10)       

cmd = "movej(get_inverse_kin(p[.056965670192, -.261001324768, .198306324642, 1.733543055982, 1.785038919736, -.830320418087], qnear=[1.5489603281021118, -2.6046579519854944, 2.545307159423828, 3.9513697624206543, 4.670498847961426, 1.4996834993362427]), a=1.3962634015954636, v=1.0471975511965976)" + "/n"
s.send (cmd.encode('utf-8'))
time.sleep(10)

#cmd = "Pose=p[0.2, 0.2, 0.2, 0, 3.14, 0]" + "\n"

#cmd = "move1(p[0, 0, 0, 0, 0, 0], a=0.5, v=0.25)" + "\n"
#s.send (cmd.encode('utf-8'))
#time.sleep(2)

#while (True):

#    cmd = "Waypoint_1" 
#    s.send (cmd.encode('utf-8'))    
#    cmd = "breakAfter"
#    s.send (cmd.encode('utf-8'))        

cmd = "movej(get_inverse_kin(p[.056965670192, -.261001324768, .198306324642, 1.733543055982, 1.785038919736, -.830320418087], qnear=[1.5489603281021118, -2.6046579519854944, 2.545307159423828, 3.9513697624206543, 4.670498847961426, 1.4996834993362427]), a=1.3962634015954636, v=1.0471975511965976)"
s.send (cmd.encode('utf-8'))
time.sleep(10)     

cmd = "/n"
s.send (cmd.encode('utf-8'))
time.sleep(15)
        
#    cmd = "Waypoint_2" 
#    s.send (cmd.encode('utf-8'))
#    cmd = "breakAfter"
#    s.send (cmd.encode('utf-8'))

cmd = "movej(get_inverse_kin(p[.310685954920, -.432811206531, .103701968061, 2.147440496121, -.860423547195, -.396913579725], qnear=[2.3123621940612793, -1.4278877417193812, 2.012190818786621, 4.051218509674072, 3.8497791290283203, -1.6746299902545374]), a=1.3962634015954636, v=1.0471975511965976)"
s.send (cmd.encode('utf-8'))
time.sleep(10)     

cmd = "/n"
s.send (cmd.encode('utf-8'))
time.sleep(15)       

#    cmd = "Waypoint_3" 
#    s.send (cmd.encode('utf-8'))
#    cmd = "breakAfter"
#    s.send (cmd.encode('utf-8'))

cmd = "movej(get_inverse_kin(p[-.004541532640, -.432805995302, .103695950707, 2.147419876637, -.860504541443, -.396957886283], qnear=[1.5077684676308325, -1.7652070487748883, 2.519217721630138, 3.229612292793827, 4.200473529849546, -2.6458979447535436]), a=1.3962634015954636, v=1.0471975511965976)"
s.send (cmd.encode('utf-8'))
time.sleep(15)
    
#    cmd = "Waypoint_2" 
#    s.send (cmd.encode('utf-8'))
#    cmd = "breakAfter"
#    s.send (cmd.encode('utf-8'))

cmd = "movej(get_inverse_kin(p[.310685954920, -.432811206531, .103701968061, 2.147440496121, -.860423547195, -.396913579725], qnear=[2.3123621940612793, -1.4278877417193812, 2.012190818786621, 4.051218509674072, 3.8497791290283203, -1.6746299902545374]), a=1.3962634015954636, v=1.0471975511965976)"
s.send (cmd.encode('utf-8'))
time.sleep(15)

#end;

cmd = "set_digital_out(2,True)" + "\n"
s.send (cmd.encode('utf-8'))
time.sleep(5)

#cmd = "set_digital_out(2,False)" + "\n"
#s.send (cmd.encode('utf-8'))
#data = s.recv(1024)

s.close()

#print('Received', repr(data))
print("Stop moving... Mission Accomplished!!!")