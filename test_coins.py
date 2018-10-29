from person import Person
from board import Board
from enemy import Enemies
from scoreboard import ScoreBoard

MB = Board(900, 40)
MB.initialise()


def test_right_coincollection():
    myscore = ScoreBoard.score
    MARIO = Person(82, -9, MB.board)
    MARIO.getcoins(MB.board,"right")
    assert ScoreBoard.score == myscore + 42

def test_left_coincollection():
    myscore = ScoreBoard.score
    MARIO = Person(84, -9, MB.board)
    MARIO.getcoins(MB.board,"left")
    assert ScoreBoard.score == myscore + 42

def test_down_coincollection():
    myscore = ScoreBoard.score
    MARIO = Person(83, -10, MB.board)
    MARIO.getcoins(MB.board,"down")
    assert ScoreBoard.score == myscore + 42
