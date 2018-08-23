import numpy as np
import signal,os,sys,time
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from scenery import DrawScenery
from enemy import BossEnemy
from scoreboard import ScoreBoard
os.system('aplay ./sounds/bg.wav')
class Board:
    
    def __init__ (self,width,height):
        self.width=width
        self.height=height
        self._screenwidth=70; #screen-width is private cannot be accessed outside the class.
        self.level = 1;

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
            Obstacles.putclouds(self.board,i,2)
        
        for i in range(self.width//3,2*self.width//3,70):
            Obstacles.putmountains(self.board,i,2)
        
        for i in range(1,(2*self.width//3-100),80):
            Obstacles.putpipes(self.board,i,-8)
        
        for i in range(1,2*self.width//3-100,40):
            self.board[-3][i] = 'S'

        for i in range(1,2*self.width//3-100,130):
            Obstacles.putbricks(self.board,i,-14,np.random.randint(2,9))
            Obstacles.putbricks(self.board,i+3,-14,np.random.randint(2,9))
        
        for i in range(90 , 2*self.width//3-100,97):
            newenemy = Enemies(self.board,i,-4,"left")
        
    def render_board(self,curx):        
        for row in range(self.height):
            for col in range(curx-self._screenwidth,curx+self._screenwidth):
                print(self.board[row][col],end="")
            print()
    
    def setlevel(self,curx,mystats):
        if(curx > 0 and curx < self.width//3):
            ScoreBoard.setlevel(mystats,1)
        if(curx >= self.width//3 and curx < 2*self.width//3):
            ScoreBoard.setlevel(mystats,2)
        if(curx >= 2*self.width//3 and curx < self.width):
            ScoreBoard.setlevel(mystats,"BOSS")

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
            if(mario.check_collision(board,"right") == "go"):
                self.x+=1;
                mario.set_mario(self.x-1,self.y,self.x,self.y,board)
                mario.checkdeath(board)

            elif(mario.check_collision(board,"right") == "dead"):
                mario.checkdeath(board,"Dead")

        if(char == 'a'):
            if(mario.check_collision(board,"left") == "go"):
                self.x-=1;
                mario.set_mario(self.x+1,self.y,self.x,self.y,board)
                mario.checkdeath(board)

            elif(mario.check_collision(board,"left") == "dead"):
                mario.checkdeath(board,"Dead")

        if(char == 'w' and mario.check_landing(board)):    
            extra = 0
            if(board[self.y+1][self.x]=='S'):
                extra+=5
            for i in range(0,15+extra):
                if(mario.check_collision(board,"up")):
                    self.y-=1;
                    mario.set_mario(self.x,self.y+1,self.x,self.y,board)
                    mario.get_brickcoins(board)
                    if(self.y == -3):
                        mario.check_kill(board)

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
                ScoreBoard.changescore(mystats,"coins")

    def checkdeath(self,board,status="Alive"):
        if(board[self.y][self.x] == 'E' or board[self.y-1][self.x] == 'E' or status == "Dead"):
           self.y -= 20;
           self.x -= 10;
           mario.set_mario(self.x+10,self.y+20,self.x,self.y,board)
           ScoreBoard.changelives(mystats) 
    
    def check_kill(self,board):
        for elements in Enemies.enemylist:
            if(mario.x == elements.x and mario.y+1 == elements.y):
                Enemies.enemylist.remove(elements)
                ScoreBoard.changescore(mystats,"enemy")

class Obstacles:  

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

    def putbricks(board,x,y,num):
        mybrick = DrawScenery.drawbricks()
        for row in range(len(mybrick)):
            for col in range(len(mybrick[row])):
                board[y+row][x+col]=mybrick[row][col];
        board[y+1][x+1]=num;
      
class Enemies:
    
    enemylist = []
    def __init__(self,board,x,y,direction):
        self.x=x;
        self.y=y;
        self.direction = direction;
        board[y][x]='E'
        Enemies.enemylist.append(self)

    def update_position(board,each_enemy):
        
        status = Enemies.collision_enemies(board,each_enemy)
        
        if(each_enemy.direction == "right" and status!="removed"):
            each_enemy.x+=1;
            board[each_enemy.y][each_enemy.x] = "E" 
            board[each_enemy.y][each_enemy.x-1] = " "

        if(each_enemy.direction == "left" and status!="removed"):
            each_enemy.x-=1;
            board[each_enemy.y][each_enemy.x] = "E" 
            board[each_enemy.y][each_enemy.x+1] = " "
            

    def collision_enemies(board,each_enemy):
        if(each_enemy.direction == "right"):
            tchar1 = board[each_enemy.y][each_enemy.x+1]
            if(tchar1 != " " and tchar1 != "\\" and tchar1 != "/" and tchar1!='M'):
                each_enemy.direction = "left"
            
        if(each_enemy.direction == "left"):
            tchar1 = board[each_enemy.y][each_enemy.x-1]
            
            if(tchar1 == "{"):
                board[each_enemy.y][each_enemy.x]=" "
                Enemies.enemylist.remove(each_enemy)
                return "removed"

            elif(tchar1 != " " and tchar1 != "\\" and tchar1 != "/" and tchar1!='M'):
                each_enemy.direction = "right"
            
class BossEnemy:
    
    def __init__(self,x,y,board):
        self.x=x
        self.y=y
        myenemy = DrawScenery.drawbossenemy()
        for row in range(len(myenemy)):
            for col in range(len(myenemy[row])):
                board[y+row][x+col]=myenemy[row][col];
    def bullets(board):
        newbullets = Enemies(board,5*mb.width//6-1,np.random.randint(-8,-4),"left")

    def eatenboss(self,board):
        myenemy = DrawScenery.drawbossenemy()
        for row in range(len(myenemy)):
            for col in range(len(myenemy[row])):
                if(board[self.y+row][self.x+col]!= " " and board[self.y+row][self.x+col]!= "M" and board[self.y+row][self.x+col]!= "\\"
                    and board[self.y+row][self.x+col]!= "/"):
                    return False
        return True

mb = Board(900,40)
mb.initialise()
mario=Person(70,-4,mb.board)
mystats=ScoreBoard()
boss=BossEnemy(5*mb.width//6,-8,mb.board)

elapsedtime = time.time()
gametime = time.time();

while True:
    os.system("clear")
    
    updatetime = time.time()
    if(updatetime - elapsedtime > 1):
        elapsedtime = updatetime
        if(np.random.randint(1,7)==3):
            BossEnemy.bullets(mb.board)
        ScoreBoard.timer(mystats)

    if(updatetime - gametime > 1/(2*float(mb.level))):
        gametime = updatetime
        for elements in Enemies.enemylist:
            Enemies.update_position(mb.board,elements)

    mario.checkdeath(mb.board)

    if(mario.y < -4 and not mario.check_landing(mb.board)):  #simulate gravity    
        mario.check_kill(mb.board)
        mario.y+=1
        mario.set_mario(mario.x,mario.y-1,mario.x,mario.y,mb.board)
    
    mb.setlevel(mario.x,mystats)
    char = mario.getchar(mb.board)
    mario.movelogic(char,mb.board)
    mb.render_board(mario.x)
    ScoreBoard.printscore(mystats)

    if(boss.eatenboss(mb.board)):
        break;

mystats.finalscore()