import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('',80))
serversocket.listen(5)

print ("Listener established on " + repr(serversocket.getsockname()))

while True:
	connection, address = serversocket.accept()
	print ("Connection accepted from" + repr(address[1]))
	connection.send("Server approved connection\n")
	connection.close()
