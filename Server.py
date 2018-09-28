from GameClass import *
from Game import *
import time

class MyLittleGameServer:

    def __init__(self):
        self.game = Game()
        self.game.initialization()
        self.f = open('log/log.txt','w')
        print("World Initialize Done!")

        self.f.writelines("World Initialize Done!\n")

    def login_check(self,name,pw):
        for a in Actor.actorlist:
            if type(a) == Player():
                if a.name == name and a.status == True:
                    if a.sec == pw:
                        a.status = False
                        