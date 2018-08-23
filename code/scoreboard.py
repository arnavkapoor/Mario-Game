class ScoreBoard():

    score = 0
    lives = 7
    time = 600
    level = 1
    

    def printscore(self):
        
        print("TIME LEFT : " + str(ScoreBoard.time)+'\n')
        print("YOUR SCORE IS : " + str(ScoreBoard.score) + '\n')
        print("LIVES LEFT : " + str(ScoreBoard.lives) + '\n')
        print("LEVEL: " + str(ScoreBoard.level) + '\n')

        if(ScoreBoard.level == "BOSS"):
            print("To defeat the boss jump and eat all the characters of the boss\n")

    def setlevel(self,levelno):
        ScoreBoard.level = levelno

    def changescore(self,capture):
        if capture == 'coins':
            ScoreBoard.score += 10  #the answer to everything....

        if capture == 'enemy':
            ScoreBoard.score += 100 

    def finalscore(self):
        ScoreBoard.score = ScoreBoard.score + ScoreBoard.time
        print('You WON, Yaaaaaaaaaaaay')
        print('Your Final Score is ' + str(ScoreBoard.score) )
 
    def changelives(self):
        ScoreBoard.lives -= 1
        
        if ScoreBoard.lives == 0:
            print('NO LIVES LEFT, GAME OVER')
            print('Your Final Score is:  ' + str(ScoreBoard.score))
            quit()
        
    def timer(self):
    
        ScoreBoard.time -= 1
       
        if ScoreBoard.time == 0:
            print("NO TIME LEFT, GAME OVER")
            quit()
        
