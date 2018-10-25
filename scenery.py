import numpy as np


class DrawScenery:
    def drawclouds():
        mycloud = []
        with open("./images/clouds.txt") as fileobj:
            for line in fileobj:
                mycloud.append(line.strip('\n'))
        return mycloud

    def drawmountains():
        mymountain = []
        with open("./images/mountains.txt") as fileobj:
            for line in fileobj:
                mymountain.append(line.strip('\n'))
        return mymountain

    def drawpipes():
        mypipes = []
        with open("./images/pipes.txt") as fileobj:
            for line in fileobj:
                mypipes.append(line.strip('\n'))
        return mypipes

    def drawbricks():
        mybricks = []
        with open("./images/bricks.txt") as fileobj:
            for line in fileobj:
                mybricks.append(line.strip('\n'))
        return mybricks

    def drawbossenemy():
        mybossenemy = []
        with open("./images/bossenemy.txt") as fileobj:
            for line in fileobj:
                mybossenemy.append(line.strip('\n'))
        return mybossenemy

    def drawsunset():
        mysunset = []
        with open("./images/sunset.txt") as fileobj:
            for line in fileobj:
                mysunset.append(line.strip('\n'))
        return mysunset
