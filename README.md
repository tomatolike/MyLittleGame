## This is a free RPG game.

### I'm tring to realize Three thing

First, players can create stories by themselves. The problem is how to give player a kind of API to generate NPC and Thing logics.

Second, players can enjoy the stories of themselves and others.

Third, players can do things with NPC or other players.

### Stage one is complete

Some basic logics, as communication, fight and trade can be generated by players.

Players can have some kinds of things to do to enjoy the stories.

Basic fight, communication and trade system has been build.

#### Some introductions to the game mechanism

The main.py is the Net I/O logic of the server.
The Game.py is the running logic of game world.
The GameClass.py is the data logic of the game.

The world is called '世界'. There are some towns in the world. Each town have its own buildings like a bar. The world, the town, the building are all 'Place'.

The players and NPCs are both 'Actor'. NPCs have their logic when they interect with players. 'Actor' can be in any 'Place'

There are 'Thing' in the world. Like 'Equipment' and 'Medic'. They can be used by 'Actor' or trade between 'Actor'.

'Actor' can communicate with each other, between a player and a player or between a player and an NPC but not between an NPC and an NPC.

'Actor' can fight with each other, between a player and a player or between a player and an NPC but not between an NPC and an NPC.

'Actor' can trade with each other, between a player and a player or between a player and an NPC but not between an NPC and an NPC.

Players can create 'Place', 'Thing', NPC and the 'Logic' of NPC. The 'Logic' is a tree of 'Action'. 'Action' is what the NPC will do. These can all be create by players. 

### Stage tow is waiting

The logic should be more general, and players should be able to design more complecated logics.

The client should be replaced by web system, which is supposed to provide players more information and more comfortable reactions with server.

The design of multithread should be cleaner.
