import signal,os
import numpy as np
from enemy import *
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from scoreboard import ScoreBoard
class Person:   
    def __init__ (self,x,y,board):
        self.x=x
        self.y=y
        board[self.y][self.x]='/'
        board[self.y-1][self.x]='M'

    def set_mario(self,prevx,prevy,curx,cury,board):
        
        board[prevy][prevx] = " "
        board[prevy-1][prevx] = " "
        if(curx%2):
            board[cury][curx] = "/"
        else:
            board[cury][curx] = '\\'
        board[cury-1][curx] = "M"

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
        
        if(char == 'd'):
            if(self.check_collision(board,"right") == "go"):
                self.getcoins(board,"right")
                self.x+=1;
                self.set_mario(self.x-1,self.y,self.x,self.y,board)
                self.checkdeath(board)

            elif(self.check_collision(board,"right") == "dead"):
                self.checkdeath(board,"Dead")

        if(char == 'a'):
            if(self.check_collision(board,"left") == "go"):
                self.getcoins(board,"left")
                self.x-=1;
                self.set_mario(self.x+1,self.y,self.x,self.y,board)
                self.checkdeath(board)

            elif(self.check_collision(board,"left") == "dead"):
                self.checkdeath(board,"Dead")

        if(char == 'w' and self.check_landing(board)):    
            os.system('aplay -q ./sounds/jump.wav&')
            extra = 0
            if(board[self.y+1][self.x]=='S'):
                extra+=5
            for i in range(0,15+extra):
                if(self.check_collision(board,"up")):
                    self.y-=1;
                    self.set_mario(self.x,self.y+1,self.x,self.y,board)
                    self.get_brickcoins(board)
                    if(self.y == -3):
                        self.check_kill(board)

        if(char == 'q'): 
            quit()

    def check_landing(self,board):
        if(board[self.y+1][self.x] == '*' or board[self.y+1][self.x]=='S'):
            return True
        return False

    def check_collision(self,board,direction):
        if(direction == "right"):
            tchar1 = board[self.y][self.x+1]
            tchar2 = board[self.y-1][self.x+1]
            if((tchar1 == " " or tchar1 == "$") and (tchar2 == " " or tchar2 == "$")):
                return "go"
            if(tchar1 == "E" or tchar2 == "E" ):
                return "dead" 
            return "stop";

        if(direction == "left"):
            tchar1 = board[self.y][self.x-1]
            tchar2 = board[self.y-1][self.x-1]
            if((tchar1 == " " or tchar1 == "$") and (tchar2 == " " or tchar2 == "$")):
                return "go"
            if(tchar1 == "E" or tchar2 == "E" ):
                return "dead" 
            return "stop";

        if(direction == "up"):
            tchar1 = board[self.y-2][self.x]
            if(tchar1 == " "):
                return True
            return False;
    
    def get_brickcoins(self,board):
        if (np.core.defchararray.isdigit(board[self.y-3][self.x])):
            val = int(board[self.y-3][self.x]);   
            if(val!=0):
                board[self.y-3][self.x] = val-1;   
                ScoreBoard.changescore("coins")

    def get
    def checkdeath(self,board,status="Alive"):
        if(board[self.y][self.x] == 'E' or board[self.y-1][self.x] == 'E' or status == "Dead"):
           self.y -= 20;
           self.x -= 10;
           self.set_mario(self.x+10,self.y+20,self.x,self.y,board)
           ScoreBoard.changelives() 
    

    
    def check_kill(self,board):
        for elements in Enemies.enemylist:
            if(self.x == elements.x and self.y+1 == elements.y):
                Enemies.enemylist.remove(elements)
                ScoreBoard.changescore("enemy")
                os.system('aplay -q ./sounds/kill.wav&')
