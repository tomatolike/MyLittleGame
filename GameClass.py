from multiprocessing import Lock
class Test:
	word = "test"

	def __init__(self):
		print("A New Test!")

	def printword(self):
		print(self.word)

# All kinds of class are inherited from this class
# Because all things or places or charactors are objects in this world
class Objects:
	# The main usage of this class is to keep a list to all objects in the world
	# Like a god
	objlist = []
	maxid = 0
	world = None

	def __init__(self):
		self.objlist.append(self)
		# Each objects in the world will be attached with a universially unique id
		# In the eyes of god, you are no different with a cup
		self.id = Objects.maxid + 1
		Objects.maxid = Objects.maxid + 1

# The architecture of places are like a tree.
# The root of the tree is '世界'
# Then, the second level of the tree is different towns, like 'Chengdu'
# Each town have some sub-places like a bar.
# Maybe in the future the second level will be province or continent
class Places(Objects):
	townlist = [] # All the towns
	allplaces = [] # All the places

	def __init__(self):
		super(Places,self).__init__()
		self.name = "name"
		self.outside = None # Where the outside is. For example, the outside of a bar is a town
		self.placescontain = [] # The places it contains. For example, a town main contain a bar
		self.placeaccount = 0 # How many places it contains
		self.actorcontain = [] # The actors it contains. For example, 'Chengdu' may contain an NPC called 'LIKE'
		self.actoraccount = 0 # How many actors it contains
		self.intro = "intro"
		Places.allplaces.append(self)

	# Print all sub-places in this place. A little like the 'ls' order in Linux file system.
	def printplaces(self):
		re = ""
		if self.placeaccount == 0:
			re += "这是个空城。"+"\n"
		else:
			for i in range(self.placeaccount):
				re += "编号："+str(i)+"；名字："+self.placescontain[i].name+"\n"
		return re

	# Print all actors in the place now, including both NPCs and players.
	# This list may change from time to time, since the players will move from places to places
	def printactors(self):
		re = ""
		if self.actoraccount == 0:
			re += "这是个鬼城。"+"\n"
		else:
			for i in range(self.actoraccount):
				re += "编号："+str(i)+"；名字："+self.actorcontain[i].name+"\n"
		return re

	# Delete an actor from the list of actors in the place. Maybe a player has moved away.
	def delone(self, actor):
		self.actoraccount = self.actoraccount - 1
		self.actorcontain.remove(actor)

	# Add an actor to the list of actors in the place.
	def addone(self, actor):
		self.actoraccount = self.actoraccount + 1
		self.actorcontain.append(actor)
		actor.where = self

	# Add a sub-place
	def addplace(self, place):
		self.placeaccount = self.placeaccount + 1
		self.placescontain.append(place)
		place.outside = self
	
	# Delete a sub-place
	def delplace(self, place):
		self.placeaccount = self.placeaccount - 1
		self.placescontain.remove(place)
		if place.outside.name == "世界":
			Places.townlist.remove(place)
		place.outside = None

# Actors. Both player and NPC are actors
# The only difference is that: players need the result of Network I/O to do action; NPCs follow the logic which we create.
# There is no relationship or 'love ratio' between players. Maybe we will add in the future.
# Anyway, Galagame should also be realised in our game.
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

# As I said, NPC has logic.
class NPC(Actor):

	def __init__(self):
		super(NPC,self).__init__()
		self.level = 0
		self.logic = None # The logic of the npc
		self.intro = "intro"
	
# The players have more parametors.
# The level of players will increase.
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

# Hey! Why do this class not inherit from Object class?
# This is because the repertory is an abstract class attached with each actor.
# This is no actually a packet on the back of each actor. You may image it like a magic packet.
# All the 'Thing's will be managed in this class.
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

# This is also an abstract class.
# This class is not an equipment class.
# It manages the equipments which the actor wear on body.
# In Chinese, '装备栏'
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

# 'Thing'!
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

# 'Equipment' is 'Thing'
class Equip(Thing):
	
	def __init__(self):
		super(Equip,self).__init__()
		self.e_type = 0 # Where to equip it
		self.useage = 2

# 'Protect' is 'Equipment'
class Protect(Equip):
	
	def __init__(self):
		super(Protect,self).__init__()
		self.amount = 0 # How much it can protect

# 'Weapon' is 'Equipment'
class Weapon(Equip):
	
	def __init__(self):
		super(Weapon,self).__init__()
		self.attack = 0 # How much it can hurt

# 'Shoes' is 'Equipment'
# This kind of equipments are mainly connected with the success of escaping!
class Shoes(Equip):
	
	def __init__(self):
		super(Shoes,self).__init__()
		self.quick = 0 # How fast it can run

# 'Medic' is 'Thing'
# Used to add HP
class Medic(Thing):

	def __init__(self):
		super(Medic,self).__init__()
		self.useage = 1
		self.amount = 0 # How much hp or fast it can cure

# Misson!
# But I have not finished the misson mechanism yet.
# Only a data class, no function yet.
class Misson(Objects):
	
	def __init__(self):
		super(Misson,self).__init__()
		self.intro = "intro"
		self.award = None # What can get from complete misson

# Logic!
# Each logic object is owned by an NPC
# Each logic object is a chain of actions
class Logic():
	
	def __init__(self):
		# Although there is a list, it is a mistake.
		# Actually, the first action is orders[0], but the second action is not orders[1].
		# This is because the actions are linked as a tree not a chain.
		# The second action (actuall, second actions), are reactions of the first action.
		# So, the list only contain one action, the first action, oders[0].
		self.orders = [] # The orders

# Actions!
# As I said, the actions are connected as a tree.
# The reactions are just like the sons of a tree node.
class Action(Objects):
	actionlist = []

	def __init__(self):
		super(Action,self).__init__()
		self.say = "say" # Say something
		self.answers = [] # Answers supported
		self.reactions = [] # Reaction to different answer
		# The first kind of action, with actiontype=0, is just saying something. The reactions of this type can be all kinds of actions.
		# The second kind of action, with actiontype=1, is asking a question. The reactions of this type can be all kinds of actions.
		# The third kind of action, with actiontype=2, is fighting with the player. No reaction.
		# The fourth kind of action, with actiontype=3, is requiring a 'Thing' from the player. This action can have two reactions, success or failure, but no limitation on reaction type.
		# The fifth kind of action, with actiontype=4, is ending the conversation. No reaction.
		# If we can define more kind of actions! We can make the game more interesting!
		# And, may be in the future, we will used machine learing to simulate the logic of NPCs.
		# Not just follow the logic tree.
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

