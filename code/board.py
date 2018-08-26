import numpy as np
import signal,os,sys,time
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from scenery import DrawScenery
from scoreboard import ScoreBoard
from person import *
from enemy import Enemies,BossEnemy
#os.system('aplay -q ./sounds/mario-theme.wav&')
class Board:
    
    def __init__ (self,width,height):
        self.width=width
        self.height=height
        self._screenwidth=70; #screen-width is private cannot be accessed outside the class.
        
    def initialise(self):
        self.board = np.empty([self.height,self.width],dtype=str)
        self.board[:,:]=" "
        self.board[-3:,0:self.width]='*'

        self.board[-17:-3,2*self.width//3]='{'
        self.board[-18:-17,2*self.width//3]='*'
        
        self.board[-3,(2*self.width//3 - 1)]='S'

        self.board[-17:-3,self.width-self._screenwidth-10]='}'
        self.board[-18:-17,self.width-self._screenwidth-10]='*'

        for i in range(1,self.width//3,45):
            Render.putclouds(self.board,i,2)
        
        for i in range(self.width//3,2*self.width//3,70):
            Render.putmountains(self.board,i,2)
        
        for i in range(1,(2*self.width//3-100),80):
            Render.putpipes(self.board,i,-9)
        
        for i in range(1,2*self.width//3-100,40):
            self.board[-3][i] = 'S'

        for i in range(1,2*self.width//3-100,130):
            Render.putbricks(self.board,i,-14,np.random.randint(2,9))
            Render.putbricks(self.board,i+3,-14,np.random.randint(2,9))
        
        for i in range(90 , 2*self.width//3-100,97):
            newenemy = Enemies(self.board,i,-4,"left")
        
        Render.putsunset(self.board,3*self.width//4+50,10)
        

    def render_board(self,curx):        
        for row in range(self.height):
            for col in range(curx-self._screenwidth,curx+self._screenwidth):
                print(self.board[row][col],end="")
            print()
    
    def setlevel(self,curx):
        if(curx > 0 and curx < self.width//3):
            ScoreBoard.setlevel(1)
        if(curx >= self.width//3 and curx < 2*self.width//3):
            ScoreBoard.setlevel(2)
        if(curx >= 2*self.width//3 and curx < self.width):
            ScoreBoard.setlevel("BOSS")


class Render:  

    def putclouds(board,x,y):
        mycloud = DrawScenery.drawclouds()
        for row in range(len(mycloud)):
            for col in range(len(mycloud[row])):
                board[y+row][x+col] = mycloud[row][col]
                 
    def putmountains(board,x,y):
        mymountain = DrawScenery.drawmountains()
        for row in range(len(mymountain)):
            for col in range(len(mymountain[row])):
                board[y+row][x+col]=mymountain[row][col];

    def putpipes(board,x,y):
        mypipe = DrawScenery.drawpipes()
        for row in range(len(mypipe)):
            for col in range(len(mypipe[row])):
                board[y+row][x+col]=mypipe[row][col];

    def putsunset(board,x,y):
        mysunset = DrawScenery.drawsunset()
        for row in range(len(mysunset)):
            for col in range(len(mysunset[row])):
                board[y+row][x+col]=mysunset[row][col];

    def putbricks(board,x,y,num):
        mybrick = DrawScenery.drawbricks()
        for row in range(len(mybrick)):
            for col in range(len(mybrick[row])):
                board[y+row][x+col]=mybrick[row][col];
        board[y+1][x+1]=num;