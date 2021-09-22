import socket
import random
#20210916
#https://docs.python.org/3/howto/sockets.html#creating-a-socket

#creating a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket only accessible to our machine and port 80
s.bind(('localhost', 80))
# listen sets the number of connection requests to queue up before refusing them
s.listen(5)

userID = 0

# current connections dictionary
userNameToSocket = {}

while True:
    # set up variables on connection
    clientsocket, (address, port) = s.accept()
    # if the socket already exists, get it's userID
    if (address,port) in userNameToSocket:
        name = userNameToSocket[(address,port)]
    # otherwise assign it the next sequential userID
    else:
        name = userID
        userNameToSocket[(address,port)] = userID
        userID+=1
    # print who connected and their userID
    print("Connection from {} started on port {}. User ID: {}".format(address,port, name))
    while clientsocket:
        # receive input
        data = clientsocket.recv(1024)
        if not data: break
        # print out the userID and the input they gave
        print("{} > {}".format(name, data))