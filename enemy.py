""" Managing the enemy class """
import scenery
import numpy as np


class Enemies:
    "Normal Enemies Class"

    enemylist = []

    def __init__(self, board, xcord, ycord, direction):
        "Initialising their direction and adding to list"

        self.xcord = xcord
        self.ycord = ycord
        self.direction = direction
        board[ycord][xcord] = 'E'
        Enemies.enemylist.append(self)

    def movelogic(self, board):
        "Code Segment to handle movement"
        status = Enemies.collision_enemies(self, board)

        if self.direction == "right" and status != "removed":
            self.xcord += 1
            board[self.ycord][self.xcord] = "E"
            board[self.ycord][self.xcord - 1] = " "

        if self.direction == "left" and status != "removed":
            self.xcord -= 1
            board[self.ycord][self.xcord] = "E"
            board[self.ycord][self.xcord + 1] = " "

    def collision_enemies(self, board):
        "Check collission of enemies with surroundings"

        if self.direction == "right":
            tchar1 = board[self.ycord][self.xcord + 1]
            if tchar1 != " " and tchar1 != "\\" and tchar1 != "/" and tchar1 != 'M':
                self.direction = "left"

        if self.direction == "left":
            tchar1 = board[self.ycord][self.xcord - 1]

            if tchar1 == "{":
                board[self.ycord][self.xcord] = " "
                Enemies.enemylist.remove(self)
                return "removed"

            elif tchar1 != " " and tchar1 != "\\" and tchar1 != "/" and tchar1 != 'M':
                self.direction = "right"


def create_bullets(board, xcord):
    "Rendering Bullets shot by boss"
    Enemies(board, xcord, np.random.randint(-8, -4), "left")


class BossEnemy:
    "Boss Enemy class"

    def __init__(self, xcord, ycord, board):
        "Intiialising Boss Enemy"

        self.xcord = xcord
        self.ycord = ycord

        myenemy = scenery.drawbossenemy()
        for row, _ in enumerate(myenemy):
            for col, _ in enumerate(myenemy[row]):
                board[ycord + row][xcord + col] = myenemy[row][col]

    def eatenboss(self, board):
        "Defeating the boss"

        myset = [" ", "M", "\\", "/"]
        myenemy = scenery.drawbossenemy()
        for row, _ in enumerate(myenemy):
            for col, _ in enumerate(myenemy[row]):
                if(board[self.ycord + row][self.xcord + col] not in myset):
                    return False
        return True
