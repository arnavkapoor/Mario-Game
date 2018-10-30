from person import Person
from board import Board
from enemy import Enemies
MB = Board(900, 40)
MB.initialise()

def test_right_collision_pipe():
    MARIO = Person(81, -4, MB.board)
    iscollide = MARIO.check_collision(MB.board,"right")
    assert iscollide == "stop"

def test_left_collision_pipe():
    MARIO = Person(89, -4, MB.board)
    iscollide = MARIO.check_collision(MB.board,"left")
    assert iscollide == "stop"

def test_right_collision_enemy():
    MARIO = Person(70, -4, MB.board)
    Enemies(MB.board, 71, -4, "left")
    iscollide = MARIO.check_collision(MB.board,"right")
    assert iscollide == "dead"

def test_left_collision_enemy():
    MARIO = Person(70, -4, MB.board)
    Enemies(MB.board, 69, -4, "left")
    iscollide = MARIO.check_collision(MB.board,"left")
    assert iscollide == "dead"