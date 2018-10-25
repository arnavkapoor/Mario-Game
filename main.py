import numpy as np
import signal
import os
import sys
import time
from getch import _getChUnix as getChar
from alarmexception import AlarmException
from scenery import DrawScenery
from scoreboard import ScoreBoard
from person import *
from enemy import Enemies, BossEnemy
from board import Board

mb = Board(900, 40)
mb.initialise()
mario = Person(70, -4, mb.board)
boss = BossEnemy(5 * mb.width // 6, -8, mb.board)

elapsedtime = time.time()
gametime = time.time()

while True:
    os.system("clear")

    updatetime = time.time()
    if(updatetime - elapsedtime > 1):
        elapsedtime = updatetime
        if(np.random.randint(1, 7) == 3):
            BossEnemy.bullets(mb.board, 5 * mb.width // 6 - 1)
        ScoreBoard.timer()
    try:
        curlev = 2 * float(ScoreBoard.level)
    except BaseException:
        curlev = 5

    if(updatetime - gametime > 1 / curlev):
        gametime = updatetime
        for elements in Enemies.enemylist:
            Enemies.movelogic(mb.board, elements)

    mario.checkdeath(mb.board)

    if(mario.y < -4 and not mario.check_landing(mb.board)):  # simulate gravity
        mario.check_kill(mb.board)
        mario.getcoins(mb.board, "down")
        mario.y += 1
        mario.set_mario(mario.x, mario.y - 1, mario.x, mario.y, mb.board)

    mb.setlevel(mario.x)
    char = mario.getchar(mb.board)
    mario.movelogic(char, mb.board)
    mb.render_board(mario.x)
    ScoreBoard.printscore()

    if(boss.eatenboss(mb.board)):
        break

ScoreBoard.finalscore()
