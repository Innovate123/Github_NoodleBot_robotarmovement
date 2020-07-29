import socket
import time

import DefinationType

def howMuchSauce(needToPut):
    if needToPut == DefinationType.no:
        return 0
    else:
        return 1

def makeNoodle(noodle):
    
    HOST = '192.168.0.100' # The remote host
    PORT = 30000           # The same port as used by the server
    
    print ("Starting Program")
    
    # Get Chilli Sauce and tomato sauce
    
    for i in noodle.listOfSauce:
        
        if i.sauceTypeId == DefinationType.chilliSauce:
            howMuchChilliSauce = howMuchSauce(i.needToPut)
                
        if i.sauceTypeId == DefinationType.tomatoSauce:
            howMuchTomatoSauce = howMuchSauce(i.needToPut)    
            
    count = 0
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print ("Connected by", addr)
    while 1:
        data = conn.recv(1024)
        print (data)
        if not data: break
        conn.send("(1,%d,%d)" % (howMuchChilliSauce, howMuchTomatoSauce))
        #conn.send("(1)")
        #conn.send("(1)")
        print ("Sending start signal to robot...")
    conn.close()
    
if __name__ == '__main__':
    noodle = ""
    makeNoodle(noodle)