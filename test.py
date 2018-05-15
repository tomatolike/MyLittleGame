import socket
import _thread
s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host,port))

s.listen(5)

def react(c, addr):
	while True:
		st = "get in server"
		c.send(str.encode(st))
		x = bytes.decode(c.recv(1024))
		print(x)
		if x == "stop":
			c.close()
			break

while True:
	c, addr = s.accept()
	print(addr)
	try:
		_thread.start_new_thread(react, (c, addr, ))
	except:
		print("Wrong!")

