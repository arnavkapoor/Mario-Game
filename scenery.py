"""Render the Scenery"""


def drawclouds():
    """draw the clouds """
    mycloud = []
    with open("./images/clouds.txt") as fileobj:
        for line in fileobj:
            mycloud.append(line.strip('\n'))
    return mycloud


def drawmountains():
    """draw the mountains """

    mymountain = []
    with open("./images/mountains.txt") as fileobj:
        for line in fileobj:
            mymountain.append(line.strip('\n'))
    return mymountain


def drawpipes():
    """draw the pipes """

    mypipes = []
    with open("./images/pipes.txt") as fileobj:
        for line in fileobj:
            mypipes.append(line.strip('\n'))
    return mypipes


def drawbricks():
    """draw the bricks """

    mybricks = []
    with open("./images/bricks.txt") as fileobj:
        for line in fileobj:
            mybricks.append(line.strip('\n'))
    return mybricks


def drawbossenemy():
    """draw the boss enemy """

    mybossenemy = []
    with open("./images/bossenemy.txt") as fileobj:
        for line in fileobj:
            mybossenemy.append(line.strip('\n'))
    return mybossenemy


def drawsunset():
    """draw the final sunset """

    mysunset = []
    with open("./images/sunset.txt") as fileobj:
        for line in fileobj:
            mysunset.append(line.strip('\n'))
    return mysunset
