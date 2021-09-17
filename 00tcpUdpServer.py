import socket
#20210916
#https://docs.python.org/3/howto/sockets.html#creating-a-socket

#creating a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket only accessible to our machine and port 80
s.bind(('localhost', 80))
# listen sets the number of connection requests to queue up before refusing them
s.listen(5)