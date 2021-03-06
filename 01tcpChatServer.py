import socket
import random
import sys
import threading

#20210922

#creating a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# allow address reuse to fix problems with having to kill process
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket only accessible to our machine and port 80
s.bind(('localhost', 80))
# listen sets the number of connection requests to queue up before refusing them
s.listen(5)

def connect():
    # set up variables on connection
    clientsocket, (address, port) = s.accept()
    # if the socket already exists, get it's userID
    print("Connection from {} started on port {}".format(address,port))
    while clientsocket:
        # receive input
        data = clientsocket.recv(1024)
        if not data: break
        # print out the userID and the input they gave
        print("{}".format(data))

def main():
   while True:
       x= threading.Thread(target=connect)
       x.start() 

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Closing')
        sys.exit(1)