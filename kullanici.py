import socket

def ihbar():

	host = "172.31.35.219"
	port = 22

	my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	my_socket.connect((host, 2346))

	data = my_socket.recv(1024)

	print(data.decode())
	my_socket.send(b"\n\n   Tehdit basariyla iletildi !!!!!")

ihbar()