#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import random
import argparse

parser = argparse.ArgumentParser(description='--player 1 argument')
parser.add_argument("--player1", required = False, help = "Choose Player 1 as Human or Computer player")
args = parser.parse_args()

parser = argparse.ArgumentParser(description='player 2 argument')
parser.add_argument("--player2", required = False, help = "Choose Player 2 as Human or Computer player")
args = parser.parse_args()

random.seed(0)

class Dice():
    def __init__(self):
        self.number = int(number)
        
    def roll(self):
        self.number = random.randint(1,6)
        return self.number
    
    
    
class Players():
    def __init__(self):
        None
            
    def P1turn(self):
        self.p1.score = 0
        self.p1curr_score = 0
        self.p1.name = "Player 1"
        if(self.dice.number == 1):
            print ("{} rolls 1, Score is zero".format(self.p1.name))
            self.p1.curr_score = 0
        else:
            self.p1score = self.p1score + self.dice.number
            print ("{} Rolled :{}".format(self.p1.name, self.dice.number))
            
        if self.p1.score >= 100:
            print ("Player 1 wins")
            print (("Player 1 Total Score:{}").format(self.p1.score))
            
    def P2turn(self):
        self.p2.score = 0
        self.p2curr_score = 0
        self.p2.name = "Player 2"
        if(self.dice.number == 1):
            print ("{} rolls 1, Score is zero".format(self.p2.name))
            self.p2.curr_score = 0
        else:
            self.p2score = self.p2score + self.dice.number
            print ("{} Rolled :{}".format(self.p2.name, self.dice.number))
            
        if self.p2.score >= 100:
            print ("Player 2 wins")
            print (("Player 2 Total Score:{}").format(self.p2.score))
            
            

class RunPigGame():
    def __init__(self, p1, p2, dice):
        self.p1 = P1turn
        self.p2 = P2turn
        self.dice = Dice()
        p1tscore = p1.score
        p2tscore = p2.score
        
        def RollorHold(self):
            RHoption = str(input("Enter r to Roll or h to hold"))
        if RHoption == 'h':
            self.roll = False
            self.hold = True
        elif RHoption == 'r':
            self.roll = True
            self.hold = False
            
        def GameOver(self):
            self.p1 = None
            self.p2 = None
            self.dice = None
            self.p1tscore = 0
            self.p2tscore = 0
        
        
        while p1score < 100 and p2score < 100:
            print ("Player 1 Score:{}".format(p1tscore))
            print ("Player 2 Score:{}".format(p2tscore))
            RollorHold(RollorHold)
            if p1.roll == True and p1.hold == False:
                self.Dice.roll
                P1turn()
            elif p1.roll == False and p1.hold == True:
                P2turn()
            elif p2.roll == True and p2.hold == False:
                self.Dice.roll
                P2turn()
            elif p2.roll == False and p2.hold == True:
                P1turn()
            else:
                GameOver()
                sys.exit
    
    
    
class ComputerPlayer(Players):
    def __init__(self):
        rp = RunPigGame(p1,p2,Dice)
        rh = rp.RollorHold()
        self.cp.score = 0
        self.cpcurr_score = 0
        self.cp.name = "Computer Player"
        if(self.dice.number == 1):
            print ("{} rolls 1, Score is zero".format(self.cp.name))
            self.cp.curr_score = 0
        else:
            self.cpscore = self.cpscore + self.dice.number
            print ("{} Rolled :{}".format(self.cp.name, self.dice.number))
        
        if 100 < self.cp.curr_score < 25:
            rh.hold = True
            rh.roll = False
        else:
            rh.hold = False
            rh.roll = True
            
        if self.cp.score >= 100:
            print ("Computer Player wins")
            print (("Computer Player Total Score:{}").format(self.cp.score))
            
            
            
class PlayerFactory(Players):
    p = Players()
    c = ComputerPlayer()
    ap1 = args.player1
    ap2 = args.player2
    def selPlayer(ap1, ap2):
        if arg.player1 == 'h':
            p.P1turn()
        elif arg.player1 == 'c':
            c.ComputerPlayer()
        if arg.player2 == 'h':
            p.P2turn()
        elif arg.player2 == 'c':
            c.ComputerPlayer()


# In[ ]:




