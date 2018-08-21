import numpy as np
import signal,os,sys,time
import random
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from scenery import *
 
class Board:
    def __init__ (self,width,height):
        self.width=width
        self.height=height
        self.screenwidth=70;

    def initialise(self):
        self.board = np.empty([self.height,self.width],dtype=str)
        self.board[:,:]=" "
        self.board[-3:,0:self.width]='*'
        self.board[-8:-6,70:140]='*'
        
        for i in range(1,self.width//3,30):
            try:
                RenderScenery.putclouds(self.board,i-random.randint(20,70),2)
            except:
                pass
        for i in range(self.width//3,2*self.width//3,70):
            try:
                RenderScenery.putmountains(self.board,i-random.randint(30,70),2)
            except:
                pass

    def render_board(self,curx):        
        for row in range(self.height):
            for col in range(curx-self.screenwidth,curx+self.screenwidth):
                print(self.board[row][col],end="")
            print()
       
            
class Person:
    def __init__ (self,x,y,board):
        self.x=x
        self.y=y
        board[self.y][self.x]='/'
        board[self.y-1][self.x]='O'

    def set_mario(self,prevx,prevy,curx,cury,board):
        
        board[prevy][prevx] = " "
        board[prevy-1][prevx] = " "
        if(curx%2):
            board[cury][curx] = "/"
        else:
            board[cury][curx] = '\\'
        board[cury-1][curx] = "O"

    def getchar(self,board):
        def alarmhandler(signum, frame):
            raise AlarmException

        def user_input(timeout=0.10):
            signal.signal(signal.SIGALRM, alarmhandler)
            signal.setitimer(signal.ITIMER_REAL, timeout)
            try:
                text = getChar()()
                signal.alarm(0)
                return text
            except AlarmException:
                pass
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return ''

        char = user_input()
        return char;

    def movelogic(self,char,board):    
        if(char == 'd' and mario.check_landing(board)):
            self.x+=1;
            mario.set_mario(self.x-1,self.y,self.x,self.y,board)
        
        if(char == 'd' and not mario.check_landing(board)):
            self.x+=2;
            mario.set_mario(self.x-2,self.y,self.x,self.y,board)
        
        if(char == 'a' and mario.check_landing(board)):
            self.x-=1;
            mario.set_mario(self.x+1,self.y,self.x,self.y,board)

        if(char == 'a' and not mario.check_landing(board)):
            self.x-=2;
            mario.set_mario(self.x+2,self.y,self.x,self.y,board)
             
        if(char == 'w' and mario.check_landing(board)):    
            for i in range(0,10):
                self.y-=1;
                mario.set_mario(self.x,self.y+1,self.x,self.y,board)

        if(char == 'q'): 
            quit()

    def check_landing(self,board):
        if(board[self.y+1][self.x] == '*'):
            return True
        return False

class RenderScenery:
    def putclouds(board,x,y):
        mycloud = DrawScenery.drawclouds()
        for row in range(len(mycloud)):
            for col in range(len(mycloud[row])):
                board[y+row][x+col]=mycloud[row][col];

    def putmountains(board,x,y):
        mymountain = DrawScenery.drawmountains()
        for row in range(len(mymountain)):
            for col in range(len(mymountain[row])):
                board[y+row][x+col]=mymountain[row][col];

mb = Board(1000,40)
mb.initialise()
mario=Person(70,-4,mb.board)
while True:
    os.system("clear")
    char = mario.getchar(mb.board)
    mario.movelogic(char,mb.board)
    
    if(mario.y < -4 and not mario.check_landing(mb.board)):     
        mario.y+=1
        mario.set_mario(mario.x,mario.y-1,mario.x,mario.y,mb.board)
    
    mb.render_board(mario.x)
