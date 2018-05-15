import socket
import _thread

s = socket.socket()
host = socket.gethostname()
#host = "10.180.19.165"
port = 12344

#print("193.112.104.61",1234)
print("连接中！")
s.connect((host,port))

def inputcheck(s):
	while True:
		x = input()
		if x == "quit":
			exit()
			break
		else:
			s.send(str.encode(x))

ok = 1

try:
	_thread.start_new_thread(inputcheck, (s,))
except:
	print("键盘监听建立失败")
	ok = 0
	s.close()

while True:
	if ok == 0:
		break
	re = bytes.decode(s.recv(1024))
	print(re)
	if re == "进入游戏失败。" or re == "你暂时离开了大陆！" or re == "登录失败":
		s.close()
		break
	
