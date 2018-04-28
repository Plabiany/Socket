import socket

HOST = '127.0.8.16'    
PORT = 6666           
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
welcome = tcp.recv(1024)
print welcome
while True:
	msg = raw_input()
	tcp.send (msg)
	answer = tcp.recv(1024)
	print answer	
tcp.close()
