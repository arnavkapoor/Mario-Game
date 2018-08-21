import numpy as np;
class DrawScenery:
    def drawclouds():
        mycloud=[]
        with open("./images/clouds.txt") as fileobj:
            for line in fileobj:  
                mycloud.append(line.strip('\n'))
        return mycloud;
    def drawmountains():
        mymountain=[]
        with open("./images/mountains.txt") as fileobj:
            for line in fileobj:  
                mymountain.append(line.strip('\n'))
        return mymountain