from scenery import DrawScenery
import numpy as np

class SupEnemies:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Enemies(SupEnemies):    
    enemylist = []
    def __init__(self,board,x,y,direction):
        super(Enemies,self).__init__(x,y)
        self.direction = direction;
        board[y][x]='E'
        Enemies.enemylist.append(self)

    def movelogic(board,each_enemy):
        
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

class BossEnemy(SupEnemies):
    
    def __init__(self,x,y,board):
        super(BossEnemy,self).__init__(x,y)
        myenemy = DrawScenery.drawbossenemy()
        for row in range(len(myenemy)):
            for col in range(len(myenemy[row])):
                board[y+row][x+col]=myenemy[row][col];
    
    def bullets(board,xcord):
        newbullets = Enemies(board,xcord,np.random.randint(-8,-4),"left")

    def eatenboss(self,board):
        myenemy = DrawScenery.drawbossenemy()
        for row in range(len(myenemy)):
            for col in range(len(myenemy[row])):
                if(board[self.y+row][self.x+col]!= " " and board[self.y+row][self.x+col]!= "M" and board[self.y+row][self.x+col]!= "\\"
                    and board[self.y+row][self.x+col]!= "/"):
                    return False
        return True

            