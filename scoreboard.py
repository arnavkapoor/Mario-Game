""" Manages the scoreboard displayed at bottom left """
import os


class ScoreBoard():
    ''' maintains the scoreboard '''
    score = 0
    lives = 7
    time = 600
    level = 1

    @classmethod
    def printscore(cls):
        ''' Prints the current score '''
        print("TIME LEFT : " + str(ScoreBoard.time) + '\n')
        print("YOUR SCORE IS : " + str(ScoreBoard.score) + '\n')
        print("LIVES LEFT : " + str(ScoreBoard.lives) + '\n')
        print("LEVEL: " + str(ScoreBoard.level) + '\n')

        if ScoreBoard.level == "BOSS":
            print("To defeat the boss jump and eat all the characters of the boss\n")

    @classmethod
    def setlevel(cls, levelno):
        ''' Sets the level '''
        ScoreBoard.level = levelno

    @classmethod
    def changescore(cls, capture):
        ''' Updates the scores '''

        if capture == 'coins':
            ScoreBoard.score += 42  # the answer to everything....

        if capture == 'enemy':
            ScoreBoard.score += 200

    @classmethod
    def finalscore(cls):
        ''' Prints the final score '''

        ScoreBoard.score = ScoreBoard.score + ScoreBoard.time
        print('You WON, Yaaaaaaaaaaaay')
        print('Your Final Score is ' + str(ScoreBoard.score))

    @classmethod
    def changelives(cls):
        ''' Updates the lives remaining '''

        ScoreBoard.lives -= 1

        if ScoreBoard.lives == 0:
            os.system('aplay -q ./sounds/gameover.wav&')
            print('NO LIVES LEFT, GAME OVER')
            print('Your Final Score is:  ' + str(ScoreBoard.score))
            os.system('pkill -kill aplay')
            quit()

    @classmethod
    def timer(cls):
        ''' Updates the time remaining '''

        ScoreBoard.time -= 1

        if ScoreBoard.time == 0:
            os.system('aplay -q ./sounds/gameover.wav&')
            print("NO TIME LEFT, GAME OVER")
            os.system('pkill -kill aplay')
            quit()
