from person import Person
from board import Board

MB = Board(900, 40)
MB.initialise()

def test_right():
    MARIO = Person(70, -4, MB.board)
    curx = MARIO.xcord    
    MARIO.movelogic('d',MB.board)
    assert MARIO.xcord == curx+1

def test_left():
    MARIO = Person(70, -4, MB.board)
    curx = MARIO.xcord    
    MARIO.movelogic('a',MB.board)
    assert MARIO.xcord == curx-1

def test_normaljump():
    
    MARIO = Person(70, -4, MB.board)
    cury = MARIO.ycord    
    MARIO.movelogic('w',MB.board)
    assert MARIO.ycord == cury-15

def test_springjump():
    MARIO = Person(70, -4, MB.board)
    MARIO.xcord = MARIO.xcord+11
    curx = MARIO.xcord    
    cury = MARIO.ycord
    MARIO.movelogic('w',MB.board)
    assert MARIO.ycord == cury-20
