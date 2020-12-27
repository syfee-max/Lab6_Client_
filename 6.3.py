import socket

ClientSocket = socket.socket()
host = '192.168.1.14'
port = 8888

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
    print('Connected!!')
except socket.error as ex:
    print(str(ex))

Response = ClientSocket.recv(1024).decode()
print(Response)

while true:
    print (' a) Logarithm \n b) Square Root \n c) Exponential Function \n e) End')
    choose = input('What do you want to do?\n ')
    
    if choose == 'a' :
        option = "1"
        value = input('What number to log?\n')
        l = option + '.' + value
        ClientSocket.send(str.encode(l))
    elif choose == 'b':
        option = "2"
        value = input('What number to square root?\n ')
        s = option + '.' + value
        ClientSocket.send(str.encode(s))
    elif choose == 'c':
        option = "3"
        value = input('Value : ')
        e = option + '.' + value 
        ClientSocket.send(str.encode(e))
    elif choose == "e":
        option = "0"
        ClientSocket.send(str.encode(option))
        print ('Thank you!! \n')
        ClientSocket.close()
    else :
        print ('Run the program \n')
        ClientSocket.close()
    Response = ClientSocket.recv(1024)
    print(Response.decode())

ClientSocket.close()