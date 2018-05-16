from GameClass import *
import random

class Game:

	def initialization(self):
		#Initialize the maxid
		self.GenerateThings()
		self.GenerateAction()
		self.GeneratePlaces()
		self.GenerateActors()
		

	def GenerateThings(self):
		print("Generating Things!")
		f = open('things.txt','r')
		while True:
			x = f.readline().strip('\n')
			if x == "END":
				break
			if x == "NEW":
				# Read the type
				x = f.readline().strip('\n')
				new = None
				if x == "Protect":
					new = Protect()
					x = f.readline().strip('\n') # Read the id
					new.id = int(x)
					x = f.readline().strip('\n') # Read the name
					new.name = x
					x = f.readline().strip('\n') # Read the intro
					new.intro = x
					x = f.readline().strip('\n') # Read the cost
					new.cost = int(x)
					x = f.readline().strip('\n') # Read the useage
					new.useage = int(x)
					x = f.readline().strip('\n') # Read the e_type
					new.e_type = int(x)
					x = f.readline().strip('\n') # Read the amount
					new.amount = int(x)

				elif x == "Weapon":
					new = Weapon()
					x = f.readline().strip('\n') # Read the id
					new.id = int(x)
					x = f.readline().strip('\n') # Read the name
					new.name = x
					x = f.readline().strip('\n') # Read the intro
					new.intro = x
					x = f.readline().strip('\n') # Read the cost
					new.cost = int(x)
					x = f.readline().strip('\n') # Read the useage
					new.useage = int(x)
					x = f.readline().strip('\n') # Read the e_type
					new.e_type = int(x)
					x = f.readline().strip('\n') # Read the attack
					new.attack = int(x)

				elif x == "Shoes":
					new = Shoes()
					x = f.readline().strip('\n') # Read the id
					new.id = int(x)
					x = f.readline().strip('\n') # Read the name
					new.name = x
					x = f.readline().strip('\n') # Read the intro
					new.intro = x
					x = f.readline().strip('\n') # Read the cost
					new.cost = int(x)
					x = f.readline().strip('\n') # Read the useage
					new.useage = int(x)
					x = f.readline().strip('\n') # Read the e_type
					new.e_type = int(x)
					x = f.readline().strip('\n') # Read the quick
					new.quick = int(x)

				elif x == "Medic":
					new = Medic()
					x = f.readline().strip('\n') # Read the id
					new.id = int(x)
					x = f.readline().strip('\n') # Read the name
					new.name = x
					x = f.readline().strip('\n') # Read the intro
					new.intro = x
					x = f.readline().strip('\n') # Read the cost
					new.cost = int(x)
					x = f.readline().strip('\n') # Read the useage
					new.useage = int(x)
					x = f.readline().strip('\n') # Read the amount
					new.amount = int(x)

				elif x == "Thing":
					new = Thing()
					x = f.readline().strip('\n') # Read the id
					new.id = int(x)
					x = f.readline().strip('\n') # Read the name
					new.name = x
					x = f.readline().strip('\n') # Read the intro
					new.intro = x
					x = f.readline().strip('\n') # Read the cost
					new.cost = int(x)
					x = f.readline().strip('\n') # Read the useage
					new.useage = int(x)

				else:
					new = Thing()
					x = f.readline().strip('\n') # Read the id
					new.id = int(x)
					x = f.readline().strip('\n') # Read the name
					new.name = x
					x = f.readline().strip('\n') # Read the intro
					new.intro = x
					x = f.readline().strip('\n') # Read the cost
					new.cost = int(x)
					x = f.readline().strip('\n') # Read the useage
					new.useage = int(x)
			x = f.readline().strip('\n')
			if x == "END":
				break
		f.close()

	def findObj(self,x):
		for a in Objects.objlist:
			if a.id == x:
				return a

	def GenerateAction(self):
		print("Generating Action!")
		f = open('action.txt','r')
		while True:
			x = f.readline().strip('\n')
			if x == "END":
				break
			if x == "NEW":
				new = Action()
				x = f.readline().strip('\n') # Read the id
				new.id = int(x)
				x = f.readline().strip('\n') # Read the say
				new.say = x
				x = f.readline().strip('\n') # Read the actiontype
				new.actiontype = int(x)
				if new.actiontype == 3:
					x = f.readline().strip('\n') # Read the thing id
					thing = self.findObj(int(x))
					new.answers.append(thing)
				else:
					x = f.readline().strip('\n') # Read the answer count
					for i in range(int(x)):
						xx = f.readline().strip('\n')
						new.answers.append(xx)
				x = f.readline().strip('\n') # Read the reaction count
				for i in range(int(x)):
					xx = f.readline().strip('\n') # Read the reaction id
					reaction = self.findObj(int(xx))
					new.reactions.append(reaction)
				
				
			x = f.readline().strip('\n')
			if x == "END":
				break
		f.close()
		Action.actionlist.reverse()

	def GenerateActors(self):
		print("Generating Actors!")
		f = open('actors.txt','r')
		while True:
			x = f.readline().strip('\n')
			if x == "END":
				break		
			if x == "NEW":
				x = f.readline().strip('\n') # Read the type
				new = None
				if x == "NPC":
					new = NPC()
					x = f.readline().strip('\n') # Read the id
					new.id = int(x)
					x = f.readline().strip('\n') # Read the name
					new.name = x
					
					x = f.readline().strip('\n') # Read the place id
					place = self.findObj(int(x))
					place.addone(new)
					new.repertory = Repertory()
					x = f.readline().strip('\n') # Read the thing count
					for i in range(int(x)):
						xx = f.readline().strip('\n') # Read the id
						thing = self.findObj(int(x))
						xx = f.readline().strip('\n') # Read the number
						for j in range(int(xx)):
							new.repertory.addup(thing)
					new.equipment = Equipment()
					for i in range(4):
						x = f.readline().strip('\n') # Read the equipment
						no = int(x)
						if no != -1:
							thing = self.findObj(int(no))
							new.equipment.equip(thing)
					x = f.readline().strip('\n') # Read the money
					new.money = int(x)
					x = f.readline().strip('\n') # Read the hp
					new.hp = int(x)
					x = f.readline().strip('\n') # Read the level
					new.level = int(x)
					new.logic = Logic()
					x = f.readline().strip('\n') # Read the first action id
					new.logic.orders.append(self.findObj(int(x)))
					x = f.readline().strip('\n') # Read the intro
					new.intro = x
				elif x == "Player":
					new = Player()
					x = f.readline().strip('\n') # Read the id
					new.id = int(x)
					print(new.id)
					x = f.readline().strip('\n') # Read the name
					new.name = x
					x = f.readline().strip('\n') # Read the place id
					place = self.findObj(int(x))
					place.addone(new)
					new.repertory = Repertory()
					x = f.readline().strip('\n') # Read the thing count
					for i in range(int(x)):
						xx = f.readline().strip('\n') # Read the id
						thing = self.findObj(int(x))
						xx = f.readline().strip('\n') # Read the number
						for j in range(int(xx)):
							new.repertory.addup(thing)
					new.equipment = Equipment()
					for i in range(4):
						x = f.readline().strip('\n') # Read the equipment
						no = int(x)
						if no != -1:
							thing = self.findObj(int(no))
							new.equipment.equip(thing)
					x = f.readline().strip('\n') # Read the money
					new.money = int(x)
					x = f.readline().strip('\n') # Read the hp
					new.hp = int(x)
					x = f.readline().strip('\n') # Read the level
					new.level = int(x)
					x = f.readline().strip('\n') # Read the exp
					new.exp = int(x)
					x = f.readline().strip('\n') # Read the sec
					new.sec = x
			x = f.readline().strip('\n')
			if x == "END":
				break
		f.close()
		for i in Actor.actorlist:
			print(i.name)
	
	def GeneratePlaces(self):
		print("Generating Places!")
		f = open('places.txt','r')
		x = f.readline().strip('\n')
		while True:
			if x == "END":
				break
			if x == "NEW":
				new = Places()
				x = f.readline().strip('\n') # Read the id
				new.id = int(x)
				x = f.readline().strip('\n') # Read the name
				new.name = x
				if new.name == "世界":
					Objects.world = new
				x = f.readline().strip('\n') # Read the outside
				no = int(x)
				if no != -1:
					outside = self.findObj(no)
					outside.addplace(new)
					if outside.name == "世界":
						Places.townlist.append(new)
				x = f.readline().strip('\n') # Read the intro
				new.intro = x
			x = f.readline().strip('\n')
			if x == "END":
				break
		f.close()

	def save(self):
		self.saveThing()
		self.saveAction()
		self.savePlaces()
		self.saveActors()

	def saveThing(self):
		print("Saving Things!")
		f = open('things.txt','w')
		for i in Thing.allthingslist:
			f.writelines("NEW"+"\n")
			if type(i) is Protect:
				f.writelines("Protect"+"\n")
				f.writelines(str(i.id)+"\n")
				f.writelines(i.name+"\n")
				f.writelines(i.intro+"\n")
				f.writelines(str(i.cost)+"\n")
				f.writelines(str(i.useage)+"\n")
				f.writelines(str(i.e_type)+"\n")
				f.writelines(str(i.amount)+"\n")
			elif type(i) is Weapon:
				f.writelines("Weapon"+"\n")
				f.writelines(str(i.id)+"\n")
				f.writelines(i.name+"\n")
				f.writelines(i.intro+"\n")
				f.writelines(str(i.cost)+"\n")
				f.writelines(str(i.useage)+"\n")
				f.writelines(str(i.e_type)+"\n")
				f.writelines(str(i.attack)+"\n")
			elif type(i) is Shoes:
				f.writelines("Shoes"+"\n")
				f.writelines(str(i.id)+"\n")
				f.writelines(i.name+"\n")
				f.writelines(i.intro+"\n")
				f.writelines(str(i.cost)+"\n")
				f.writelines(str(i.useage)+"\n")
				f.writelines(str(i.e_type)+"\n")
				f.writelines(str(i.quick)+"\n")
			elif type(i) is Medic:
				f.writelines("Medic"+"\n")
				f.writelines(str(i.id)+"\n")
				f.writelines(i.name+"\n")
				f.writelines(i.intro+"\n")
				f.writelines(str(i.cost)+"\n")
				f.writelines(str(i.useage)+"\n")
				f.writelines(str(i.amount)+"\n")
			elif type(i) is Thing:
				f.writelines("Thing"+"\n")
				f.writelines(str(i.id)+"\n")
				f.writelines(i.name+"\n")
				f.writelines(i.intro+"\n")
				f.writelines(str(i.cost)+"\n")
				f.writelines(str(i.useage)+"\n")
			else:
				pass
			f.writelines(""+"\n")
		f.writelines("END"+"\n")
		f.close()

	def saveAction(self):
		print("Saving Actions!")
		Action.actionlist.reverse()
		f = open('action.txt','w')
		for i in Action.actionlist:
			f.writelines("NEW"+"\n")
			f.writelines(str(i.id)+"\n")
			f.writelines(i.say+"\n")
			f.writelines(str(i.actiontype)+"\n")
			if i.actiontype == 3:
				f.writelines(str(i.answers[0].id)+"\n")
			else:
				f.writelines(str(len(i.answers))+"\n")
				for x in i.answers:
					f.writelines(x+"\n")
			f.writelines(str(len(i.reactions))+"\n")
			for x in i.reactions:
				f.writelines(str(x.id)+"\n")
			f.writelines(""+"\n")
		f.writelines("END"+"\n")
		f.close()
		Action.actionlist.reverse()

	def savePlaces(self):
		print("Saving Places!")
		f = open('places.txt','w')
		for i in Places.allplaces:
			f.writelines("NEW"+"\n")
			f.writelines(str(i.id)+"\n")
			f.writelines(i.name+"\n")
			if i.outside == None:
				f.writelines("-1"+"\n")
			else:
				f.writelines(str(i.outside.id)+"\n")
			f.writelines(i.intro+"\n")
			f.writelines(""+"\n")
		f.writelines("END"+"\n")
		f.close()

	def saveActors(self):
		print("Saving Actors!")
		f = open('actors.txt','w')
		for i in Actor.actorlist:
			f.writelines("NEW"+"\n")
			if type(i) is NPC:
				f.writelines("NPC"+"\n")
				f.writelines(str(i.id)+"\n")
				f.writelines(i.name+"\n")
				f.writelines(str(i.where.id)+"\n")
				f.writelines(str(i.repertory.account)+"\n")
				for j in range(i.repertory.account):
					f.writelines(str(i.repertory.things[j].id)+"\n")
					f.writelines(str(i.repertory.amount[j])+"\n")
				if i.equipment.head != None:
					f.writelines(str(i.equipment.head.id)+"\n")
				else:
					f.writelines("-1"+"\n")
				if i.equipment.body != None:
					f.writelines(str(i.equipment.body.id)+"\n")
				else:
					f.writelines("-1"+"\n")
				if i.equipment.hand != None:
					f.writelines(str(i.equipment.hand.id)+"\n")
				else:
					f.writelines("-1"+"\n")
				if i.equipment.foot != None:
					f.writelines(str(i.equipment.foot.id)+"\n")
				else:
					f.writelines("-1"+"\n")
				f.writelines(str(i.money)+"\n")
				f.writelines(str(i.hp)+"\n")
				f.writelines(str(i.level)+"\n")
				f.writelines(str(i.logic.orders[0].id)+"\n")
				f.writelines(i.intro+"\n")
			elif type(i) is Player:
				f.writelines("Player"+"\n")
				f.writelines(str(i.id)+"\n")
				f.writelines(i.name+"\n")
				f.writelines(str(i.where.id)+"\n")
				f.writelines(str(i.repertory.account)+"\n")
				for j in range(i.repertory.account):
					f.writelines(str(i.repertory.things[j].id)+"\n")
					f.writelines(str(i.repertory.amount[j])+"\n")
				if i.equipment.head != None:
					f.writelines(str(i.equipment.head.id)+"\n")
				else:
					f.writelines("-1"+"\n")
				if i.equipment.body != None:
					f.writelines(str(i.equipment.body.id)+"\n")
				else:
					f.writelines("-1"+"\n")
				if i.equipment.hand != None:
					f.writelines(str(i.equipment.hand.id)+"\n")
				else:
					f.writelines("-1"+"\n")
				if i.equipment.foot != None:
					f.writelines(str(i.equipment.foot.id)+"\n")
				else:
					f.writelines("-1"+"\n")
				f.writelines(str(i.money)+"\n")
				f.writelines(str(i.hp)+"\n")
				f.writelines(str(i.level)+"\n")
				f.writelines(str(i.exp)+"\n")
				f.writelines(i.sec+"\n")
			else:
				pass
			f.writelines(""+"\n")
		f.writelines("END"+"\n")
		f.close()



	def prints(self, a, s):
		a.net.prints(s)

	def inputs(self, a, s=""):
		return a.net.inputs(s)

	def GetInLogic(self, a, b):
		a.busy.acquire()
		if b.logic == None:
			self.prints(a,b.name+"是一个沉默寡言的人。")
			a.busy.release()
			return
		if not (b.logic.orders):
			self.prints(a,b.name+"是一个沉默寡言的人。")
			a.busy.release()
			return
		action = b.logic.orders[0]
		while True:
			if action.actiontype == 0:
				self.prints(a,b.name+"说：")
				self.prints(a,action.saytheword())
				action = action.reactions[0]
			elif action.actiontype == 1:
				self.prints(a,b.name+"说：")
				self.prints(a,action.saytheword())
				self.prints(a,action.printanswers())
				answer = self.inputs(a,"请回复0~"+str(len(action.answers))+"：");
				to = -1
				try:
					to = int(answer)
				except:
					to = -1
				if to < 0 or to == len(action.answers):
					self.prints(a,"你不好好说话，"+b.name+"不理你了。")
					break
				action = action.reactions[to]
				
			elif action.actiontype == 3:
				self.prints(a,"你和"+b.name+"开始获取物品。")
				if action.answers[0] in a.repertory.things:
					c = a.repertory.things.index(action.answers[0])
					self.swap(a,b,c)
					action = action.reactions[0]
				else:
					self.prints(a,"你没有这个东西")
					action = action.reactions[1]
				
			elif action.actiontype == 2:
				self.prints(a,"你和"+b.name+"进入了战斗！")
				self.GetInFight(a,b)
				break
			elif action.actiontype == 4:
				self.prints(a,"谈话结束。")
				break
			else:
				self.prints(a,b.name+"不知道在干嘛。")
				break
		a.busy.release()

	def GetInChat(self, a, b):
		a.busy.acquire()
		b.busy.acquire()
		self.prints(b,a.name+"想和你交谈，同意吗？")
		answer = self.inputs(b,"回复1：拒绝；回复2：同意：")
		if answer == "1":
			self.prints(a,"对方拒绝了。")
			a.busy.release()
			b.busy.release()
			return
		elif answer != "2":
			self.prints(b,"乱输入！就当你拒绝了！")
			self.prints(a,"对方拒绝了。")
			a.busy.release()
			b.busy.release()
			return
		else:
			self.prints(a,"你和"+b.name+"进入了交谈")
			self.prints(b,"你和"+a.name+"进入了交谈")

		while True:
			self.prints(a,"请"+a.name+"发言！输入exit退出交谈。")
			self.prints(b,"请"+a.name+"发言！")
			answer = self.inputs(a)
			if answer == "exit":
				self.prints(a,"你退出了交谈")
				self.prints(b,"对方退出了交谈")
				a.busy.release()
				b.busy.release()
				return
			self.prints(b,a.name+"说："+answer)
			self.prints(a,"请"+b.name+"发言！")
			self.prints(b,"请"+b.name+"发言！输入exit退出交谈。")
			answer = self.inputs(b)
			if answer == "exit":
				self.prints(b,"你退出了交谈")
				self.prints(a,"对方退出了交谈")
				a.busy.release()
				b.busy.release()
				return
			self.prints(a,b.name+"说："+answer)


	def GetInTrade(self, a, b):
		a.busy.acquire()
		if type(b) is Player:
			b.busy.acquire()
			self.prints(b,a.name+"想和你交易，是否同意？")
			answer = self.inputs(b,"回复1：拒绝；回复2：同意：")
			if answer == "1":
				self.prints(a,"对方拒绝了。")
				a.busy.release()
				b.busy.release()
				return
			elif answer != "2":
				self.prints(b,"乱输入！就当你拒绝了！")
				self.prints(a,"对方拒绝了。")
				a.busy.release()
				b.busy.release()
				return
			else:
				self.prints(a,"你和"+b.name+"进入了交易。")
				self.prints(b,"你和"+a.name+"进入了交易。")


		if type(a) is Player:
			answer = self.inputs(a,"想买还是卖？1、买；2、卖:")
			if answer == "1":
				self.prints(a,b.name+"有这些东西：")
				self.prints(a,b.repertory.listall())
				answer1 = self.inputs(a,"请输入你想要的物品编号：")
				answer2 = self.inputs(a,"请输入你愿意支付的金额：")
				no = -1
				try:
					no = int(answer1)
				except:
					no = -1
				price = -1
				try:
					price = int(answer2)
				except:
					price = -1
				if price > a.money:
					self.prints(a,"没钱别玩儿。")
					a.busy.release()
					if type(b) is Player:
						b.busy.release()
					return
				if no >= len(b.repertory.things) or no < 0:
					self.prints(a,"别乱输入。")
					if type(b) is Player:
						b.busy.release()
					return

				if type(b) is NPC:
					if price > b.repertory.things[no].cost * (random.randint(95,105)/100):
						self.swap(b,a,no)
						a.money -= price
						b.money += price
					else:
						self.prints(a,"对方拒绝了。")
				else:
					self.prints(b,a.name+"想要用"+str(answer2)+"元换你的"+b.repertory.things[no].name)
					answer = self.inputs(b,"回复1：拒绝；回复2：同意：")
					if answer == "1":
						self.prints(a,"对方拒绝了。")
					elif answer == "2":
						self.swap(b,a,no)
						a.money -= price
						b.money += price
				a.busy.release()
				if type(b) is Player:
					b.busy.release()
			elif answer == "2":
				self.prints(a,"你有这些东西：")
				self.prints(a,a.repertory.listall())
				answer1 = self.inputs(a,"请输入你想卖的物品编号：")
				answer2 = self.inputs(a,"请输入你希望得到的金额：")
				no = -1
				try:
					no = int(answer1)
				except:
					no = -1
				price = -1
				try:
					price = int(answer2)
				except:
					price = -1
				if price < b.money:
					self.prints(a,"他没有那么多钱。")
					a.busy.release()
					if type(b) is Player:
						b.busy.release()
					return
				if no < 0 or no >= len(a.repertory.things):
					self.prints(a,"别乱输入。")
					a.busy.release()
					if type(b) is Player:
						b.busy.release()
					return

				if type(b) is NPC:
					if price < a.repertory.things[no].cost * (random.randint(95,105)/100):
						self.swap(a,b,no)
						a.money += price
						b.money -= price
					else:
						self.prints(a,"对方拒绝了。")
				else:
					self.prints(b,a.name+"想要用"+a.repertory.things[no].name+"换你的"+str(answer2+"元。\n"))
					answer = self.inputs(b,"回复1：拒绝；回复2：同意：")
					if answer == "1":
						self.prints(a,"对方拒绝了。")
					elif answer == "2":
						self.swap(a,b,no)
						a.money += price
						b.money -= price
				a.busy.release()
				if type(b) is Player:
					b.busy.release()
			else:
				self.prints(a,"别乱输入。")
				a.busy.release()
				if type(b) is Player:
					self.prints(b,"对方退出了")
					b.busy.release()
		

	def GetInFight(self, a, b):
		a.busy.acquire()
		self.prints(a,"等待对方进入战斗……")
		if type(b) is Player:
			b.busy.acquire()
			self.prints(b,"你和"+a.name+"进入了战斗！。")
		self.prints(a,"对方进入战斗！")

		turn = 1
		while True:
			if turn == 1:
				now = b
				theother = a
			else:
				now = a
				theother = b

			if type(now) is NPC:
				self.doattack(now,theother)
			else:
				self.prints(now,"你要做什么？\n回复1：攻击\n回复2：使用物品\n回复3：逃跑\n回复4：投降")
				answer = self.inputs(now,"请回复1~3：")
				if answer == "1":
					self.doattack(now,theother)
				elif answer == "2":
					self.usething(now)
				elif answer == "3":
					ok = self.escape(now,theother)
					if ok == 1:
						self.prints(now,"你逃走了")
						now.busy.release()
						if type(theother) is Player:
							self.prints(theother,"对方逃走了")
							theother.busy.release()
						return
					else:
						self.prints(now,"你没逃走。")
				elif answer == "4":
					now.hp = 0
					self.prints(now,"你投降了。")
					if type(theother) is Player:
						self.prints(theother,"对方投降了。")
				else:
					self.prints(now,"你什么都没做。")

			turn = 1 - turn

			if now.hp <= 0:
				self.winner(theother, now)
				break

			if theother.hp <=0:
				self.winner(now, theother)
				break
			else:
				if type(now) is not NPC:
					self.prints(now,"\n" + now.name + " hp :" + str(now.hp))
					self.prints(now,theother.name + " hp :" + str(theother.hp) + "\n")
				if type(theother) is not NPC:
					self.prints(theother,"\n" + now.name + " hp :" + str(now.hp))
					self.prints(theother,theother.name + " hp :" + str(theother.hp) + "\n")

		a.busy.release()
		if type(b) is Player:
			b.busy.release()


	def doattack(self, a, b):
		if a.equipment == None:
			attack = 0
		else:
			if a.equipment.hand == None:
				attack = 0
			else:
				if b.equipment == None:
					attack = a.equipment.hand.attack
				else:
					attack = a.equipment.hand.attack*(random.randint(90,110)/100)
					if b.equipment.foot != None:
						if random.randint(1,100) < b.equipment.foot.quick:
							attack = 0
					if b.equipment.head != None:
						attack = attack*(1 - (b.equipment.head.amount/100)*(random.randint(50,100)/100))
					if b.equipment.body != None:
						attack = attack*(1 - (b.equipment.body.amount/100)*(random.randint(50,100)/100))
		if type(a) is Player:
			self.prints(a,"你造成了"+str(attack)+"点伤害。\n")

		if type(b) is Player:
			self.prints(b,"你受到了"+str(attack)+"点伤害。\n")

		b.hp = b.hp - attack

	def usething(self,a):
		if a.repertory == None:
			self.prints(a,"你没有背包。")
			return

		self.prints(a,"你有这些东西可以用：")
		self.prints(a,a.repertory.listall())
		answer = self.inputs(a,"回复使用物品的编号来使用：")
		to = -1
		try:
			to = int(answer)
		except:
			to = -1

		if to<0 or to>=len(a.repertory.things):
			self.prints(a,"别乱用没有的东西。")
			return

		if a.repertory.things[to].useage == 0:
			self.prints(a,"不可以使用。")
			return
		elif a.repertory.things[to].useage == 1:
			a.hp = a.hp + a.repertory.things[to].amount
			if a.hp > 100 + a.level:
				a.hp = 100 + a.level
			self.prints(a,"你的hp已回复到"+str(a.hp))
			a.repertory.reduse(to)
			return
		elif a.repertory.things[to].useage == 2:
			if a.equipment != None:
				www = a.equipment.equip(a.repertory.things[to])
				if(www == ""):
					self.prints(a,"你装备了"+a.repertory.things[to].name)
					a.repertory.reduse(to)
				else:
					self.prints(a,www)
					
		else:
			self.prints(a,"坏东西。")

	def escape(self, a, b):
		if a.equipment != None:
			if a.equipment.foot != None:
				if b.equipment == None:
					return 1
				if b.equipment.foot == None:
					return 1
				if b.equipment.foot.quick < a.equipment.foot.quick:
					return 1
		return 0

	def winner(self, a, b):
		if type(a) is NPC:
			a.hp = 100 + a.level
			a.money += b.money/10
		else:
			self.prints(a,"你获胜了！")
			a.money += b.money/10
			a.addexp(b.level + 1)

		if type(b) is NPC:
			b.hp = 100 + b.level
			b.money -= b.money
		else:
			self.prints(b,"你失败了！")
			b.money -= b.money/10
			b.hp = 1

		self.swap(b,a,-1)

	def swap(self,a,b,c):
		if c == -1:
			if a.repertory == None or a.repertory.account == 0:
				return
			x = random.randint(0,len(a.repertory.things)-1)
			it = a.repertory.things[x]
			if it != None:
				if type(a) is Player:
					self.prints(a,"你失去了"+it.name)
				a.repertory.reduse(x)
				if type(b) is Player:
					self.prints(b,"你获得了"+it.name)
				b.repertory.addup(it)

		elif c>=0 and c<a.repertory.account:
			it = a.repertory.things[c]
			if type(a) is Player:
				self.prints(a,"你失去了"+it.name)
			a.repertory.reduse(c)
			if type(b) is Player:
				self.prints(b,"你获得了"+it.name)
			b.repertory.addup(it)

	def createActor(self, a):
		a.busy.acquire()
		new = NPC()
		answer = self.inputs(a,"请输入人物名称：")
		new.name = answer
		new.where = a.where
		a.where.addone(new)
		new.repertory = Repertory()
		new.equipment = Equipment()

		while True:
			answer = self.inputs(a,"请输入人物初始金额：")
			ok = 1
			try:
				new.money = int(answer)
			except:
				ok = 0
			if new.money < 0:
				ok = 0
			if ok == 0:
				self.prints(a, "非法输入。")
			else:
				break

		while True:
			answer = self.inputs(a,"请输入人物等级：")
			ok = 1
			try:
				new.level = int(answer)
			except:
				ok = 0
			if new.level < 0:
				ok = 0
			if ok == 0:
				self.prints(a, "非法输入。")
			else:
				break
		answer = self.inputs(a,"请输入人物介绍：")
		new.intro = answer

		self.prints(a,"\n现在开始建立人物逻辑：\n")
		new.logic = Logic()
		x = self.buildAction("一开始", a)
		new.logic.orders.append(x)
		self.prints(a,"\n人物逻辑建立完毕。\n")

		while True:
			self.prints(a,"人物可拥有下列物品：")
			self.prints(a,Thing.listall())
			self.prints(a,"输入编号使其拥有或输入-1结束：")
			answer = self.inputs(a)
			no = -2
			try:
				no = int(answer)
			except:
				no = -2
			if no == -1:
				break
			elif no < 0 or no >= len(Thing.allthingslist):
				self.prints(a, "非法输入啦！")
			else:
				new.repertory.addup(Thing.allthingslist[no])
				self.prints(a,new.name+"获得"+Thing.allthingslist[no].name)

		while True:
			self.prints(a,"人物可装备下列物品：")
			self.prints(a,Thing.listall())
			self.prints(a,"输入编号使其拥有或输入-1结束：")
			answer = self.inputs(a)
			no = -2
			try:
				no = int(answer)
			except:
				no = -2
			if no == -1:
				break
			elif no < 0 or no >= len(Thing.allthingslist):
				self.prints(a, "非法输入啦！")
			else:
				www = new.equipment.equip(Thing.allthingslist[no])
				if www == "":
					self.prints(a,new.name+"装备"+Thing.allthingslist[no].name)
				else:
					self.prints(a,www)


		self.prints(a,"人物建立完毕。")
		a.busy.release()

	def buildAction(self, a, b):
		self.prints(b,"针对"+a+"要做什么？")
		action = Action()
		while True:
			self.prints(b,"1、陈述\n2、提问\n3、进入战斗\n4、获取物品\n5、结束对话\n")
			answer = self.inputs(b,"请回复1~5：")
			ok = 1
			try:
				action.actiontype = int(answer) - 1
			except:
				ok = 0
			if action.actiontype < 0 or action.actiontype > 4:
				ok = 0
			if ok == 0:
				self.prints(b, "非法输入啦！")
			else:
				break

		if action.actiontype == 0:
			answer = self.inputs(b,"请输入要陈述的内容：")
			action.say = answer
			rec = self.buildAction(answer, b)
			action.reactions.append(rec)

		elif action.actiontype == 1:
			answer = self.inputs(b,"请输入要问的问题：")
			action.say = answer
			no = 0
			while True:
				answer = self.inputs(b,"请输入回答个数：")
				ok = 1
				try:
					no = int(answer)
				except:
					ok = 0
				if no<1:
					ok = 0
				if ok == 0 :
					self.prints(b,"非法输入啦！")
				else:
					break

			for i in range(no):
				answer = self.inputs(b,"请输入第"+str(i)+"个回答的内容：")
				action.answers.append(answer[:])
				rec = self.buildAction(answer[:], b)
				action.reactions.append(rec)
				

		elif action.actiontype == 3:
			no = 0
			while True:
				self.prints(b,"可向交谈者获取下列物品：")
				self.prints(b,Thing.listall())
				self.prints(b,"输入编号：")
				answer = self.inputs(b)
				try:
					no = int(answer)
				except:
					no = -1
				if no < 0 or no >= len(Thing.allthingslist):
					print("非法输入啦！")
				else:
					break
			action.answers.append(Thing.allthingslist[no])
			action.say = "获取"+Thing.allthingslist[no].name
			rec = self.buildAction(action.say+"成功", b)
			action.reactions.append(rec)
			rec = self.buildAction(action.say+"失败", b)
			action.reactions.append(rec)

		else:
			action.say = "不用说。"

		return action

	def createPlace(self, a):
		a.busy.acquire()
		new = Places()
		answer = self.inputs(a,"请输入地点名称：")
		new.name = answer
		new.outside = a.where
		if a.where.name == "世界":
			new.townlist.append(new)
		a.where.addplace(new)
		answer = self.inputs(a,"请输入地点介绍：")
		new.intro = answer

		self.prints(a,"地点建立完毕。")
		a.busy.release()

	def createThing(self, a):
		a.busy.acquire()
		self.prints(a,"请输入物品种类：\n1、头盔\n2、盔甲\n3、武器\n4、鞋子\n5、药物\n6、其他\n")
		answer = self.inputs(a,"请回复1~6：")

		if answer == "1":
			new = Protect()
			new.e_type = 0
			answer = self.inputs(a,"请输入名称：")
			new.name = answer
			answer = self.inputs(a,"请输入介绍：")
			new.intro = answer
			while True:
				answer = self.inputs(a,"请输入防御值：")
				ok = 1
				try:
					new.amount = int(answer)
				except:
					ok = 0
				if new.amount < 0:
					ok = 0
				if ok ==0:
					self.prints(a,"请输入正确的数值！")
				else:
					break
			new.cost = new.amount*100

		elif answer == "2":
			new = Protect()
			new.e_type = 1
			answer = self.inputs(a,"请输入名称：")
			new.name = answer
			answer = self.inputs(a,"请输入介绍：")
			new.intro = answer
			while True:
				answer = self.inputs(a,"请输入防御值：")
				ok = 1
				try:
					new.amount = int(answer)
				except:
					ok = 0
				if new.amount < 0:
					ok = 0
				if ok ==0:
					self.prints(a,"请输入正确的数值！")
				else:
					break
			new.cost = new.amount*100

		elif answer == "3":
			new = Weapon()
			new.e_type = 2
			answer = self.inputs(a,"请输入名称：")
			new.name = answer
			answer = self.inputs(a,"请输入介绍：")
			new.intro = answer
			while True:
				answer = self.inputs(a,"请输入攻击值：")
				ok = 1
				try:
					new.attack = int(answer)
				except:
					ok = 0
				if new.attack < 0:
					ok = 0
				if ok ==0:
					self.prints(a,"请输入正确的数值！")
				else:
					break
			new.cost = new.attack*100

		elif answer == "4":
			new = Shoes()
			new.e_type = 3
			answer = self.inputs(a,"请输入名称：")
			new.name = answer
			answer = self.inputs(a,"请输入介绍：")
			new.intro = answer
			while True:
				answer = self.inputs(a,"请输入敏捷值：")
				ok = 1
				try:
					new.quick = int(answer)
				except:
					ok = 0
				if new.quick < 0:
					ok = 0
				if ok ==0:
					self.prints(a,"请输入正确的数值！")
				else:
					break
			new.cost = new.quick*100

		elif answer == "5":
			new = Medic()
			new.e_type = 0
			answer = self.inputs(a,"请输入名称：")
			new.name = answer
			answer = self.inputs(a,"请输入介绍：")
			new.intro = answer
			while True:
				answer = self.inputs(a,"请输入hp恢复值：")
				ok = 1
				try:
					new.amount = int(answer)
				except:
					ok = 0
				if new.amount < 0:
					ok = 0
				if ok ==0:
					self.prints(a,"请输入正确的数值！")
				else:
					break
			new.cost = new.amount*100

		elif answer == "6":
			new = Thing()
			new.e_type = 0
			answer = self.inputs(a,"请输入名称：")
			new.name = answer
			answer = self.inputs(a,"请输入介绍：")
			new.intro = answer
			while True:
				answer = self.inputs(a,"请输入价格：")
				ok = 1
				try:
					new.cost = int(answer)
				except:
					ok = 0
				if new.cost < 0:
					ok = 0
				if ok ==0:
					self.prints(a,"请输入正确的数值！")
				else:
					break

		else:
			self.prints(a,"好好说话。")
			a.busy.release()
			return

		while True:
			self.prints(a,"这些NPC可以拥有它：")
			self.prints(a,Actor.listallNPC())
			self.prints(a,"输入编号使其拥有或输入-1结束：")
			answer = self.inputs(a)
			no = -2
			try:
				no = int(answer)
			except:
				no = -2

			if no == -1:
				break
			elif no < 0 or no >= len(Actor.actorlist):
				self.prints(a,"请输入正确的编号！")
			else:
				if type(Actor.actorlist[no]) is NPC:
					Actor.actorlist[no].repertory.addup(new)

		self.prints(a,"物品建立完毕。")
		a.busy.release()





		



