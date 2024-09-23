import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'chal.pctf.competitivecyber.club'
port = 6001
secretLength = 14

s.connect((host, port))
print(s.recv(8192))
print()
#connect and recieve welcome message

s.recv(8192) #void useless info

secretString = "0123456789abcde"
solveString = "0123456789abcde"
chars = "1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()-=_+{}[]|\\:\",.<>/?"

for i in range (secretLength): 

    s.sendall(secretString.encode())
    secretHash = str(s.recv(1024))
    secretHash = secretHash.split('>')[1]
    secretHash = secretHash[1:]
    secretHash = secretHash.split('\\')[0]
    secretHash = secretHash[0:31]
    #sends the secret string with N letters missing
    #and trims the output to only the first pad
    #this gives the hash for our string with the
    #first N letters of the secret at the end

    for c in chars :
        
        s.sendall((solveString+c).encode())
        solveHash = str(s.recv(1024))
        s.recv(1024) #voiding useless info
        solveHash = solveHash.split('>')[1]
        solveHash = solveHash[1:]
        solveHash = solveHash.split('\\')[0]
        solveHash = solveHash[0:31]
        #we now send the base string with
        #every char appended to it until we get a 
        #matching hash
        
        if (solveHash == secretHash) :
            secretString = secretString[1:]
            solveString = solveString[1:]+c
            print(solveString)
            break
        #once a match is found we remove the first letter
        #of both strings and append the secret char to our
        #newstring so now the currstring has 15-N chars
        #and new string has N secret chars at the end of it

print(solveString[2:])
