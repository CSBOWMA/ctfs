import base64
import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'chal.pctf.competitivecyber.club'
port = 9001
iteration = 0
val = ""
val2 = 0
s.connect((host, port))

print(s.recv(8192)) #the initial welcome message
print()

while iteration < 1000 :

    time.sleep(.05) #the program does not work consistenly without this
    chal = str(s.recv(8192))
   
    chal = chal.split(' ')[1]
    chal = chal.split('\\')[0];
    chal = str(base64.b64decode(chal))
    #cleaning the message and then decoding

    chal = chal.split('|')
    val = chal[1] 
    chal = chal[0]
    #the decoded message contains a base64 string
    #encoded N times and then the value of N
    #this splits it into those two components

    val2 = int(val[:-1])

    chal = chal.split('\'')[1]
    chal = str(chal)
    #more cleaning removes the beginning

    for i in range(int(val2)):
        chal = base64.b64decode(chal).decode()
    #decodes N times

    chal = f"{chal}|{iteration}"
    print(chal)
    s.sendall(chal.encode()) 
    #finally sends the final message with
    #the end string and current iteration

    chal = ""
    val = ""
    val2= 0
    iteration += 1

chal = str(s.recv(16192))
print(chal)
