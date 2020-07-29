import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def instructionForTheRobot(movementList):
    for msg in movementList:
        s.send(msg[0].encode())
        time.sleep(i[1])
        


# Create a list to store the waypoint and wait time
listOfMovement = []
# Each group will store the string waypoint and integer wait time in seconds in order
listOfMovement.append(["Instruction for the waypoint 1",1])
listOfMovement.append(["Instruction for the waypoint 2",2])
listOfMovement.append(["Instruction for the waypoint 3",3])

# Let the thing run first
instructionForTheRobot(listOfMovement)
                    
                    
                    