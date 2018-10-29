from person import Person
from board import Board
from enemy import Enemies
from scoreboard import ScoreBoard
import os
MB = Board(900, 40)
MB.initialise()


def test_music():
    os.system('aplay -q ./sounds/mario-theme.wav&')
    MARIO = Person(82, -9, MB.board)
    MARIO.movelogic('q', MB.board,"test")
    ret = os.system('pkill -kill aplay')
    print(ret)
