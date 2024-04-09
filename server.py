from datetime import datetime
import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #creating a socket 

host = socket.gethostname()
port = 9990

serversocket.bind(host,port)

serversocket.listen(5)

