""" Main Mario Functionality"""
import signal
import os
import numpy as np
from enemy import Enemies
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from scoreboard import ScoreBoard


class Person:
    """ Initialising Mario Class """

    def __init__(self, xcord, ycord, board):
        self.xcord = xcord
        self.ycord = ycord
        board[self.ycord][self.xcord] = '/'
        board[self.ycord - 1][self.xcord] = 'M'

    def set_mario(self, prevx, prevy, curx, cury, board):
        """ Set The Co-ordinated of Mario """

        board[prevy][prevx] = " "
        board[prevy - 1][prevx] = " "
        if curx % 2:
            board[cury][curx] = "/"
        else:
            board[cury][curx] = '\\'
        board[cury - 1][curx] = "M"

    def getchar(self, board):
        def alarmhandler(signum, frame):
            raise AlarmException

        def user_input(timeout=0.10):
            """ Taking in User Input """

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
        return char

    def movelogic(self, char, board):
        """ Moving character based on input """

        if char == 'd':
            if self.check_collision(board, "right") == "go":
                self.getcoins(board, "right")
                self.xcord += 1
                self.set_mario(
                    self.xcord - 1,
                    self.ycord,
                    self.xcord,
                    self.ycord,
                    board)
                self.checkdeath(board)

            elif self.check_collision(board, "right") == "dead":
                self.checkdeath(board, "Dead")

        if char == 'a':
            if self.check_collision(board, "left") == "go":
                self.getcoins(board, "left")
                self.xcord -= 1
                self.set_mario(
                    self.xcord + 1,
                    self.ycord,
                    self.xcord,
                    self.ycord,
                    board)
                self.checkdeath(board)

            elif self.check_collision(board, "left") == "dead":
                self.checkdeath(board, "Dead")

        if char == 'w' and self.check_landing(board):
            os.system('aplay -q ./sounds/jump.wav&')
            extra = 0
            if board[self.ycord + 1][self.xcord] == 'S':
                extra += 5
            for _ in range(0, 15 + extra):
                if self.check_collision(board, "up"):
                    self.ycord -= 1
                    self.set_mario(
                        self.xcord,
                        self.ycord + 1,
                        self.xcord,
                        self.ycord,
                        board)
                    self.get_brickcoins(board)
                    if self.ycord == -3:
                        self.check_kill()

        if char == 'q':
            quit()

    def check_landing(self, board):
        """ checking landing """
        if board[self.ycord +
                 1][self.xcord] == '*' or board[self.ycord +
                                                1][self.xcord] == 'S':
            return True
        return False

    def check_collision(self, board, direction):
        """ collision of mario with surroundings """

        if direction == "right":
            tchar1 = board[self.ycord][self.xcord + 1]
            tchar2 = board[self.ycord - 1][self.xcord + 1]
            if (tchar1 == " " or tchar1 == "$") and (
                    tchar2 == " " or tchar2 == "$"):
                return "go"
            if tchar1 == "E" or tchar2 == "E":
                return "dead"
            return "stop"

        if direction == "left":
            tchar1 = board[self.ycord][self.xcord - 1]
            tchar2 = board[self.ycord - 1][self.xcord - 1]
            if (tchar1 == " " or tchar1 == "$") and (
                    tchar2 == " " or tchar2 == "$"):
                return "go"
            if tchar1 == "E" or tchar2 == "E":
                return "dead"
            return "stop"

        if direction == "up":
            tchar1 = board[self.ycord - 2][self.xcord]
            if tchar1 == " ":
                return True
            return False

    def get_brickcoins(self, board):
        """ Get coins by hitting bricks """

        if np.core.defchararray.isdigit(board[self.ycord - 3][self.xcord]):
            val = int(board[self.ycord - 3][self.xcord])
            if val != 0:
                board[self.ycord - 3][self.xcord] = val - 1
                ScoreBoard.changescore("coins")

    def getcoins(self, board, direction):
        """ Normal Bricks """

        if direction == "right":
            if board[self.ycord][self.xcord + 1] == '$':
                ScoreBoard.changescore("coins")
                os.system('aplay -q ./sounds/coins.wav&')

        if direction == "left":
            if board[self.ycord][self.xcord - 1] == '$':
                ScoreBoard.changescore("coins")
                os.system('aplay -q ./sounds/coins.wav&')

        if direction == "down":
            if board[self.ycord + 1][self.xcord] == '$':
                ScoreBoard.changescore("coins")
                os.system('aplay -q ./sounds/coins.wav&')

    def checkdeath(self, board, status="Alive"):
        """ Check death i.e collision with Enemies """

        if board[self.ycord][self.xcord] == 'E' or board[self.ycord -
                                                         1][self.xcord] == 'E' or status == "Dead":
            self.ycord -= 20
            self.xcord -= 10
            self.set_mario(
                self.xcord + 10,
                self.ycord + 20,
                self.xcord,
                self.ycord,
                board)
            ScoreBoard.changelives()

    def check_kill(self):
        """ Check killing of enemies """

        for elements in Enemies.enemylist:
            if self.xcord == elements.xcord and self.ycord + 1 == elements.ycord:
                Enemies.enemylist.remove(elements)
                ScoreBoard.changescore("enemy")
                os.system('aplay -q ./sounds/kill.wav&')
