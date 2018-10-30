""" The main board rendered for the gameplay uses individual
rendenring objects fuctions to populate the board """

import os
import numpy as np
import scenery
from scoreboard import ScoreBoard
from enemy import Enemies

os.system('aplay -q ./sounds/mario-theme.wav&')


class Board:
    """ The main playing board class  """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        # screen-width is private cannot be accessed outside the class.
        self._screenwidth = 70
        self.board = []
        self.board = np.empty([self.height, self.width], dtype=str)
        self.board[:, :] = " "

    def initialise(self):
        """ Initialising and popoulating the board """

        self.board[-3:, 0:self.width] = '*'

        self.board[-17:-3, 2 * self.width // 3] = '{'
        self.board[-18:-17, 2 * self.width // 3] = '*'

        self.board[-3, (2 * self.width // 3 - 1)] = 'S'

        self.board[-17:-3, self.width - self._screenwidth - 10] = '}'
        self.board[-18:-17, self.width - self._screenwidth - 10] = '*'

        for i in range(1, self.width // 3, 45):
            putclouds(self.board, i, 2)

        for i in range(self.width // 3, 2 * self.width // 3, 70):
            putmountains(self.board, i, 2)

        for i in range(1, (2 * self.width // 3 - 100), 80):
            putpipes(self.board, i, -9)

        for i in range(1, 2 * self.width // 3 - 100, 40):
            self.board[-3][i] = 'S'

        for i in range(1, 2 * self.width // 3 - 100, 130):
            putbricks(self.board, i, -14, np.random.randint(2, 9))
            putbricks(self.board, i + 3, -14, np.random.randint(2, 9))

        for i in range(90, 2 * self.width // 3 - 100, 97):
            Enemies(self.board, i, -4, "left")

        putsunset(self.board, 3 * self.width // 4 + 50, 10)

    def render_board(self, curx):
        """ Printing the board """

        for row in range(self.height):
            for col in range(
                    curx - self._screenwidth,
                    curx + self._screenwidth):
                print(self.board[row][col], end="")
            print()

    def setlevel(self, curx):
        """ Setting the current difficulty level """

        if curx > 0 and curx < self.width // 3:
            ScoreBoard.setlevel(1)
        if curx >= self.width // 3 and curx < 2 * self.width // 3:
            ScoreBoard.setlevel(2)
        if curx >= 2 * self.width // 3 and curx < self.width:
            ScoreBoard.setlevel("BOSS")


def putclouds(board, xcord, ycord):
    """ puts clouds in the scenery """

    mycloud = scenery.drawclouds()
    for row, _ in enumerate(mycloud):
        for col, _ in enumerate(mycloud[row]):
            board[ycord + row][xcord + col] = mycloud[row][col]


def putmountains(board, xcord, ycord):
    """ puts mountains in the scenery """

    mymountain = scenery.drawmountains()
    for row, _ in enumerate(mymountain):
        for col, _ in enumerate(mymountain[row]):
            board[ycord + row][xcord + col] = mymountain[row][col]


def putpipes(board, xcord, ycord):
    """ puts pipes in the scenery """

    mypipe = scenery.drawpipes()
    for row, _ in enumerate(mypipe):
        for col, _ in enumerate(mypipe[row]):
            board[ycord + row][xcord + col] = mypipe[row][col]


def putsunset(board, xcord, ycord):
    """ puts sunset in the scenery """

    mysunset = scenery.drawsunset()
    for row, _ in enumerate(mysunset):
        for col, _ in enumerate(mysunset[row]):
            board[ycord + row][xcord + col] = mysunset[row][col]


def putbricks(board, xcord, ycord, num):
    """ puts bricks in the scenery """

    mybrick = scenery.drawbricks()
    for row, _ in enumerate(mybrick):
        for col, _ in enumerate(mybrick[row]):
            board[ycord + row][xcord + col] = mybrick[row][col]
    board[ycord + 1][xcord + 1] = num
