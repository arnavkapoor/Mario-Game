import numpy as np
import signal,os,sys,time
from getch import _getChUnix as getChar
from alarmexception import AlarmException


''' The Board Class :
The board class creates a 18x18 board for gameplay,
with boundaries, walls and empty spaces. It also
comprises of a getprint function to take a print
of the board.'''


class Board:
    def __init__ (self,width,height):
        self.width=width
        self.height=height
        self.screenwidth=70;

    def initialise(self):
        self.board = np.empty([self.height,self.width],dtype=str)
        self.board[:,:]=" "
        self.board[-3:,0:210]='*'
        

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

        def user_input(timeout=0.05):
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
        if(char == 'd'):
            self.x+=1;
            mario.set_mario(self.x-1,self.y,self.x,self.y,board)

        if(char == 'a'):
            self.x-=1;
            mario.set_mario(self.x+1,self.y,self.x,self.y,board)

        if(char == 'w'):    
            for i in range(0,10):
                self.y-=1;
                mario.set_mario(self.x,self.y+1,self.x,self.y,board)
        
        if(char == 'q'): 
        	quit()
           
    
mb = Board(1000,40)
mb.initialise()
mario=Person(70,-4,mb.board)

while True:
    os.system("clear")
    char = mario.getchar(mb.board)
    mario.movelogic(char,mb.board)

    if(mario.y < -4):     
        mario.y+=1
        mario.set_mario(mario.x,mario.y-1,mario.x,mario.y,mb.board)
    
    mb.render_board(mario.x)
