""" the main game loop that calls each of the different functions """

import os
import time
import numpy as np
from scoreboard import ScoreBoard
from person import Person
from enemy import Enemies, BossEnemy
from enemy import create_bullets
from board import Board

MB = Board(900, 40)
MB.initialise()
MARIO = Person(70, -4, MB.board)
BOSS = BossEnemy(5 * MB.width // 6, -8, MB.board)

ELAPSED_TIME = time.time()
GAME_TIME = time.time()

while True:

    os.system("clear")

    UPDATE_TIME = time.time()
    if UPDATE_TIME - ELAPSED_TIME > 1:
        ELAPSED_TIME = UPDATE_TIME
        if np.random.randint(1, 7) == 3:
            create_bullets(MB.board, 5 * MB.width // 6 - 1)
        ScoreBoard.timer()
    try:
        CURLEV = 2 * float(ScoreBoard.level)
    except BaseException:
        CURLEV = 5

    if UPDATE_TIME - GAME_TIME > 1 / CURLEV:
        GAME_TIME = UPDATE_TIME
        for elements in Enemies.enemylist:
            elements.movelogic(MB.board)

    MARIO.checkdeath(MB.board)

    if MARIO.ycord < - \
            4 and not MARIO.check_landing(MB.board):  # simulate gravity
        MARIO.check_kill()
        MARIO.getcoins(MB.board, "down")
        MARIO.ycord += 1
        MARIO.set_mario(
            MARIO.xcord,
            MARIO.ycord - 1,
            MARIO.xcord,
            MARIO.ycord,
            MB.board)

    MB.setlevel(MARIO.xcord)
    CHAR = MARIO.getchar(MB.board)
    MARIO.movelogic(CHAR, MB.board)
    MB.render_board(MARIO.xcord)
    ScoreBoard.printscore()

    if BOSS.eatenboss(MB.board):
        break

ScoreBoard.finalscore()
