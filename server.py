import socket
import time
from tqdm import tqdm
import os

os.system("cls")

print("\n\n   Server Kruluyor....")
print("\n")
islemler = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]

for i in tqdm(islemler):
	time.sleep(0.1)

print("\n\n   Server kuruldu.")
time.sleep(3)

os.system("cls")

print("\n\n   DEMIR Server")

while True:

	host = "localhost"
	port = 4646

	my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	my_socket.bind((host, 2346))
	my_socket.listen(1)
	
	con, addr = my_socket.accept()
	con.send(b"\n\n   Tehdit algilandi")

	data = con.recv(1024)
	
	print(data.decode())
