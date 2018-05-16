from multiprocessing import Lock
class Test:
	word = "test"

	def __init__(self):
		print("A New Test!")

	def printword(self):
		print(self.word)


class Objects:
	objlist = []
	maxid = 0
	world = None

	def __init__(self):
		self.objlist.append(self)
		self.id = Objects.maxid + 1
		Objects.maxid = Objects.maxid + 1
		#print(Objects.maxid)

class Places(Objects):
	townlist = [] # All the towns
	allplaces = []

	def __init__(self):
		super(Places,self).__init__()
		self.name = "name"
		self.outside = None # Where the outside is
		self.placescontain = [] # The places it contains
		self.placeaccount = 0 # How many places it contains
		self.actorcontain = [] # The actors it contains
		self.actoraccount = 0 # How many actors it contains
		self.intro = "intro"
		Places.allplaces.append(self)

	def printplaces(self):
		re = ""
		if self.placeaccount == 0:
			re += "这是个空城。"+"\n"
		else:
			for i in range(self.placeaccount):
				re += "编号："+str(i)+"；名字："+self.placescontain[i].name+"\n"
		return re

	def printactors(self):
		re = ""
		if self.actoraccount == 0:
			re += "这是个鬼城。"+"\n"
		else:
			for i in range(self.actoraccount):
				re += "编号："+str(i)+"；名字："+self.actorcontain[i].name+"\n"
		return re

	def delone(self, actor):
		self.actoraccount = self.actoraccount - 1
		self.actorcontain.remove(actor)

	def addone(self, actor):
		self.actoraccount = self.actoraccount + 1
		self.actorcontain.append(actor)
		actor.where = self

	def addplace(self, place):
		self.placeaccount = self.placeaccount + 1
		self.placescontain.append(place)
		place.outside = self

	def delplace(self, place):
		self.placeaccount = self.placeaccount - 1
		self.placescontain.remove(place)
		if place.outside.name == "世界":
			Places.townlist.remove(place)
		place.outside = None

class Actor(Objects):
	actorlist = []

	def __init__(self):
		super(Actor,self).__init__()
		self.name = "name"
		self.where = None # Where the actor is
		self.repertory = None # His repertory
		self.equipment = None # The equipments he get
		self.money = 0 # Money he get
		self.hp = 100 # Health
		Actor.actorlist.append(self)

	@staticmethod
	def listallNPC():
		re = ""
		for i in range(len(Actor.actorlist)):
			if type(Actor.actorlist[i]) is NPC:
				re += "编号"+str(i)+"："+Actor.actorlist[i].name+"\n"
		return re

	def printwhere(self): # Print where he is
		re = ""
		if self.where == None:
			re += "你在：天堂。"+"\n"
		else:
			re += "你在："+self.where.name+"。"+"\n"
		return re

	def printrepertory(self):
		re = ""
		if self.repertory == None:
			re += "你连背包都没有。"+"\n"
		else:
			re += self.repertory.listall()
		return re

	def printequipment(self):
		re = ""
		if self.equipment == None:
			re += "你只是个灵魂。"+"\n"
		else:
			re += self.equipment.listall()
		return re

	def goto(self, a, b):
		re = ""
		if self.where == None:
			re += "你在天堂。"+"\n"
			return re
		fr = self.where
		if a == 1:
			to = self.where.placescontain[b]
		elif a == 2:
			if self.where.outside == None:
				re += "你出不去了。"+"\n"
				return re
			else:
				to = self.where.outside
		elif a == 3:
			to = Places.townlist[b]

		fr.delone(self)
		to.addone(self)
		self.where = to
		re += "你来到了："+self.where.name+"\n"
		return re


class NPC(Actor):

	def __init__(self):
		super(NPC,self).__init__()
		self.level = 0
		self.logic = None # The logic of the npc
		self.intro = "intro"
	

class Player(Actor):
	
	def __init__(self):
		super(Player,self).__init__()
		self.level = 0
		self.exp = 0
		self.sec = "123456"
		self.status = True
		self.net = None
		self.waiting = False
		self.busy = Lock()

	def printbasic(self): # Print basic info of him
		re = ""
		re += "名字："+self.name+"\n"
		re += "金钱："+str(self.money)+"\n"
		re += "生命值："+str(self.hp)+"\n"
		re += "等级："+str(self.level)+"\n"
		re += "经验："+str(self.exp)+"/"+str((self.level+1)*100)+"\n"
		return re

	def addexp(self, a):
		self.exp += a
		if self.exp >= (self.level+1)*100:
			self.exp -= (self.level+1)*100
			self.level += 1

class Repertory():

	def __init__(self):
		self.things = [] # Things in repertory
		self.amount = [] # The amount of each thing
		self.account = 0 # How many things it has

	def listall(self):
		re = ""
		if self.account == 0:
			re += "啥都没有。"+"\n"
		else:
			for i in range(self.account):
				re += "编号："+str(i)+"；名字："+self.things[i].name+"；价格："+str(self.things[i].cost)+"；数量："+str(self.amount[i])+"\n"
		return re

	def reduse(self, a):
		self.amount[a] = self.amount[a] - 1
		if self.amount[a] == 0 :
			self.amount.remove(self.amount[a])
			self.things.remove(self.things[a])
		self.account = len(self.things)

	def addup(self, a):
		if a in self.things:
			self.amount[self.things.index(a)] += 1
		else:
			self.things.append(a)
			self.amount.append(1)
		self.account = len(self.things)

class Equipment():
	
	def __init__(self):
		self.head = None # The thing on head
		self.body = None # The thing on body
		self.hand = None # The thing on hand
		self.foot = None # The thing on foot

	def listall(self):
		re = ""
		if self.head == None:
			re += "光头。"+"\n"
		else:
			re += "头上："+self.head.name+"\n"

		if self.body == None:
			re += "裸体。"+"\n"
		else:
			re += "身上："+self.body.name+"\n"

		if self.hand == None:
			re += "空手。"+"\n"
		else:
			re += "手上："+self.hand.name+"\n"

		if self.foot == None:
			re += "赤足。"+"\n"
		else:
			re += "脚上："+self.foot.name+"\n"
		return re

	def equip(self, a):
		re = ""
		if type(a) is not Protect and type(a) is not Weapon and type(a) is not Shoes:
			re += "无法装备。"+"\n"
			return re
		if a.e_type == 0:
			if self.head != None:
				re += "你需要先卸下头上的东西。"+"\n"
				return re
			self.head = a
			return re
		elif a.e_type == 1:
			if self.body != None:
				re += "你需要先卸下身上的东西。"+"\n"
				return re
			self.body = a
			return re
		elif a.e_type == 2:
			if self.hand != None:
				re += "你需要先卸下手上的东西。"+"\n"
				return re
			self.hand = a
			return re
		elif a.e_type == 3:
			if self.foot != None:
				re += "你需要先卸下脚上的东西。"+"\n"
				return re
			self.foot = a
			return re
		else:
			return "无效装备。"

	def unequip(self, a, b):
		re = ""
		if b == 0 and a.equipment.head != None:
			a.repertory.addup(a.equipment.head)
			re += "你卸下了"+a.equipment.head.name+"\n"
			a.equipment.head = None
		elif b == 1 and a.equipment.body != None:
			a.repertory.addup(a.equipment.body)
			re += "你卸下了"+a.equipment.body.name+"\n"
			a.equipment.body = None
		elif b == 2 and a.equipment.hand != None:
			a.repertory.addup(a.equipment.hand)
			re += "你卸下了"+a.equipment.hand.name+"\n"
			a.equipment.hand = None
		elif b == 3 and a.equipment.foot != None:
			a.repertory.addup(a.equipment.foot)
			re += "你卸下了"+a.equipment.foot.name+"\n"
			a.equipment.foot = None
		else:
			re += "卸下失败"+"\n"
		return re

class Thing(Objects):
	allthingslist = []
	
	def __init__(self):
		super(Thing,self).__init__()
		self.name = "name"
		self.intro = "intro"
		self.cost = 0
		self.useage = 0 # The useage of the thing
		Thing.allthingslist.append(self)

	@staticmethod
	def listall():
		re = ""
		for i in range(len(Thing.allthingslist)):
			re += "编号"+str(i)+"："+Thing.allthingslist[i].name+"\n"
		return re

class Equip(Thing):
	
	def __init__(self):
		super(Equip,self).__init__()
		self.e_type = 0 # Where to equip it
		self.useage = 2

class Protect(Equip):
	
	def __init__(self):
		super(Protect,self).__init__()
		self.amount = 0 # How much it can protect


class Weapon(Equip):
	
	def __init__(self):
		super(Weapon,self).__init__()
		self.attack = 0 # How much it can hurt


class Shoes(Equip):
	
	def __init__(self):
		super(Shoes,self).__init__()
		self.quick = 0 # How fast it can run

class Medic(Thing):

	def __init__(self):
		super(Medic,self).__init__()
		self.useage = 1
		self.amount = 0 # How much hp or fast it can cure

class Misson(Objects):
	
	def __init__(self):
		super(Misson,self).__init__()
		self.intro = "intro"
		self.award = None # What can get from complete misson


class Logic():
	
	def __init__(self):
		self.orders = [] # The orders

class Action(Objects):
	actionlist = []

	def __init__(self):
		super(Action,self).__init__()
		self.say = "say" # Say something
		self.answers = [] # Answers supported
		self.reactions = [] # Reaction to different answer
		self.actiontype = 0 # The type of action
		Action.actionlist.append(self)

	def saytheword(self):
		re = ""
		re += self.say+"\n"+"\n"
		return re

	def printanswers(self):
		re = ""
		if not (self.answers):
			re += "没有可以回的话。\n"+"\n"
		else:
			for i in range(len(self.answers)):
				re += "回复"+str(i)+"："+self.answers[i]
		return re

