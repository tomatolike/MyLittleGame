from GameClass import *
from Game import *
import socket
import _thread

Game = Game()
Game.initialization()

f = open('log.txt','w')

print("世界建立完成！")
f.writelines("世界建立完成！\n")

class MainConnect:

	def __init__(self,c,addr):
		print("连接点建立中……")
		f.writelines("连接点建立中……\n")
		self.c = c
		self.addr = addr
		self.actor = None
		print("连接点建立结束！")
		f.writelines("连接点建立结束！\n")

	def prints(self, s):
		#s = s+"\n"
		self.c.send(str.encode(s))

	def inputs(self, s=""):
		if s != "":
			#s = s+"\n"
			self.c.send(str.encode(s))
		x = bytes.decode(self.c.recv(1024))
		return x

	def login(self):
		answer = self.inputs("请输入角色名（账号）：")
		for a in Actor.actorlist:
			if a.name == answer and a.status == True:
				answer = self.inputs("请输入密码：")
				if a.sec == answer:
					self.actor = a
					a.status = False
					a.net = self
					print(a.name+"登录成功！")
					f.writelines(a.name+"登陆成功！\n")
					return True
		print("登录失败")
		f.writelines("登录失败\n")
		return False


	def mainprocess(self):

		while True:

			self.prints("\n\n#####################\n")
			self.prints("欢迎来到 神秘大陆 ！")
			self.prints("你要做什么？\n你可以选择：\n回复1：查看自己的信息\n回复2：前往一个地方\n回复3：找这里的人做事\n回复4：使用物品\n回复5：创造\n回复6：离开")
			answer = self.inputs("请回复1~6：");

			if answer == "1":
				self.prints("你想查看：\n1：自己所在的位置；2：自己的基本信息；3：自己拥有的物品\n")
				answer = self.inputs("请回复1~3：");

				if answer == "1":
					self.prints(self.actor.printwhere())
					continue
				elif answer == "2":
					self.prints(self.actor.printbasic())
					continue
				elif answer == "3":
					self.prints("你想查看：\n1：背包；2：身上穿的；\n")
					answer = self.inputs("请回复1~2：");

					if answer == "1":
						self.prints(self.actor.printrepertory())
						continue
					elif answer == "2":
						self.prints(self.actor.printequipment())
						self.prints("\n卸下装备？1、是；2、否：")
						answer = self.inputs()
						if answer == "1":
							answer = self.inputs("卸下：1、头盔；2、盔甲；3、武器；4、鞋子：")
							no = int(answer)
							self.prints(self.actor.equipment.unequip(self.actor,no-1))
						continue
					else:
						self.prints("好好说话行吗。")
				else:
					self.prints("好好说话行吗。")

			
			elif answer == "2":
				self.prints("你想去：\n1：这里的地点；2：外面；3：其他城镇\n")
				answer = self.inputs("请回复1~3：");

				if answer == "1":
					if self.actor.where == None:
						self.prints("你在天堂呢。")
						continue

					self.prints("这里有如下一些地点：")
					self.prints(self.actor.where.printplaces())
					answer = self.inputs("请回复编号：");
					to = int(answer)
					if to < 0 or to >= self.actor.where.placeaccount:
						self.prints("好好说话行吗。")
					else:
						self.prints(self.actor.goto(1,to))
				elif answer == "2":
					self.prints(self.actor.goto(2,0))
				elif answer == "3":
					self.prints("这个世界有如下一些城镇：")
					world = Objects.world
					self.prints(world.printplaces())
					answer = self.inputs("请回复编号：");
					to = int(answer)
					if to < 0 or to >= world.placeaccount:
						self.prints("好好说话行吗？")
					else:
						self.prints(self.actor.goto(3,to))

			elif answer == "3":
				self.prints("这里有这些人：\n")
				self.prints(self.actor.where.printactors())

				answer = self.inputs("请回复编号：");
				to = int(answer)
				if self.actor.where.actorcontain[to] == self.actor:
					self.prints("自己找自己干嘛！")
					continue
				else:
					whom = self.actor.where.actorcontain[to]
					self.prints("你找到了"+whom.name+"\n")
					self.prints("你想要：\n回复1：交谈\n回复2：战斗\n回复3：交易\n")

					answer = self.inputs("请回复1~3：");

					if answer == "1":
						if type(whom) is NPC:
							self.prints("你开始了交谈：\n")
							Game.GetInLogic(self.actor,whom)
							continue
						elif type(whom) is Player and whom.status == False:
							Game.GetInChat(self.actor,whom)
							continue
						else:
							self.prints("这个人不存在或不在线！")
					elif answer == "2":
						if type(whom) is NPC:
							self.prints("你开始了战斗！\n")
							Game.GetInFight(self.actor,whom)
						elif type(whom) is Player and whom.status == False:
							self.prints("你开始了战斗！\n")
							Game.GetInFight(self.actor,whom)
						else:
							self.prints("这个人不存在或不在线！")
					elif answer == "3":
						if type(whom) is NPC:
							self.prints("你开始了交易！\n")
							Game.GetInTrade(self.actor,whom)
						elif type(whom) is Player and whom.status == False:
							self.prints("你开始了交易！\n")
							Game.GetInTrade(self.actor,whom)
						else:
							self.prints("这个人不存在或不在线！")
								
					else:
						self.prints("好好说话！")

			elif answer == "4":
				Game.usething(self.actor)

			elif answer == "5":
				self.prints("你可以创造：\n回复1：在当前位置的新人物\n回复2：在当前地点下的新地点\n回复3：物品\n")
				answer = self.inputs("请回复1~3：")

				if answer == "1":
					Game.createActor(self.actor)
				elif answer == "2":
					Game.createPlace(self.actor)
				elif answer == "3":
					Game.createThing(self.actor)
				else:
					self.prints("好好说话。")

			elif answer == "6":
				self.prints("你暂时离开了大陆！")
				self.actor.status = True
				break

			else:
				self.prints("好好说话。")

		self.end()

	def end(self):
		print(self.actor.name+"退出游戏")
		f.writelines(self.actor.name+"退出游戏\n")
		cc = self.c
		self.c = None
		cc.close()


def connectgame(c, addr):
	print("尝试建立连接点")
	f.writelines("尝试建立连接点"+"\n")
	newplay = MainConnect(c,addr)
	print("建立连接点完毕")
	f.writelines("建立连接点完毕\n")
	if newplay.login():
		newplay.mainprocess()
	else:
		c.send(str.encode("登录失败"))
		c.close()


s = socket.socket()
def startupserver():
	#host = socket.gethostname()
	host = '10.186.46.50'
	port = 12344
	s.bind((host,port))

	s.listen(5)

	print("开始监听")
	f.writelines("开始监听\n")

	while True:
		c, addr = s.accept()
		print(addr,end=" connected!\n")
		try:
			_thread.start_new_thread(connectgame, (c,addr,))
			
		except:
			c.send(str.encode("进入游戏失败。"))
			c.close()

try:
	print("尝试建立服务器")
	f.writelines("尝试建立服务器\n")
	_thread.start_new_thread(startupserver, ())
except:
	print("服务器建立失败")
	f.writelines("服务器建立失败\n")

while True:
	x = input()
	if x == "stop":
		s.close()
		Game.save()
		f.close()
		exit()
	if x == "save":
		Game.save()








