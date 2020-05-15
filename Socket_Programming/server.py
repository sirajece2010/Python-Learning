#!/usr/bin/python3
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444
serversocket.bind((host,port))

serversocket.listen(5)

while True:
    clientsocket, address = serversocket.accept()
    print ("Received connection from "+ str(address) + clientsocket)
    message = 'hello\r\n'
    clientsocket.send(message)
    clientsocket.close()
