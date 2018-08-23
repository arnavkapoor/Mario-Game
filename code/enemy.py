class BossEnemy:
    def drawbossenemy():
        mybossenemy=[]
        with open("./images/bossenemy.txt") as fileobj:
            for line in fileobj:  
                mybossenemy.append('\x1b[0;34m'+line.strip('\n')+'\x1b[0m')
        
        return mybossenemy;