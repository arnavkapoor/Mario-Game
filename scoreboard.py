import os


class ScoreBoard():

    score = 0
    lives = 7
    time = 600
    level = 1

    def printscore():

        print("TIME LEFT : " + str(ScoreBoard.time) + '\n')
        print("YOUR SCORE IS : " + str(ScoreBoard.score) + '\n')
        print("LIVES LEFT : " + str(ScoreBoard.lives) + '\n')
        print("LEVEL: " + str(ScoreBoard.level) + '\n')

        if(ScoreBoard.level == "BOSS"):
            print("To defeat the boss jump and eat all the characters of the boss\n")

    def setlevel(levelno):
        ScoreBoard.level = levelno

    def changescore(capture):
        if capture == 'coins':
            ScoreBoard.score += 42  # the answer to everything....

        if capture == 'enemy':
            ScoreBoard.score += 200

    def finalscore():
        ScoreBoard.score = ScoreBoard.score + ScoreBoard.time
        print('You WON, Yaaaaaaaaaaaay')
        print('Your Final Score is ' + str(ScoreBoard.score))

    def changelives():
        ScoreBoard.lives -= 1

        if ScoreBoard.lives == 0:
            os.system('aplay -q ./sounds/gameover.wav&')
            print('NO LIVES LEFT, GAME OVER')
            print('Your Final Score is:  ' + str(ScoreBoard.score))
            os.system('pkill -kill aplay')
            quit()

    def timer():

        ScoreBoard.time -= 1

        if ScoreBoard.time == 0:
            os.system('aplay -q ./sounds/gameover.wav&')
            print("NO TIME LEFT, GAME OVER")
            os.system('pkill -kill aplay')
            quit()
