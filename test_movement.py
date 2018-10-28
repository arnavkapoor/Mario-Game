from person import Person
from board import Board

MB = Board(900, 40)
MB.initialise()
MARIO = Person(70, -4, MB.board)

def test_right():
    curx = MARIO.xcord    
    MARIO.movelogic('d',MB.board)
    assert MARIO.xcord == curx+1
    
#test_right()
