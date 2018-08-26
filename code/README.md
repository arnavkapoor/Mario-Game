About the Game
-------------------
> - Browse this link for info : https://en.wikipedia.org/wiki/Super_Mario_Bros

Rules of the Game
-------------------

> - You control Mario acoss various obstacles and fight enemies.
> - Enemies are undergoing random walk, but *contact* with them can kill your Mario.
> - You have 7 lives for your Mario, getting killed 7 times will result in a **GAME OVER**.
> - The Mario can lay bombs that will kill enemies and destroy bricks in a limited range from where the bomb is planted, the walls remain unaffected. 
> - Each coin adds 42 points to the score, while killing each enemy adds 200 points.
> - Level 1 - Has clouds in the background and slowest speed enemy
> - Level 2 - Has mountains in the background and medium speed enemy
> - Boss Level - Has a boss with fastest speed enemy. 
> - The Boss Level is a unique level where the boss randomly shoots bullets (having the same feature as the enemy at you). To defeat the boss you need to eat and overwrite all the characters of the boss.


Description of Classes Created
--------------------------------------------
####Board:
The board class creates the entire grid.

####Draw Scenery:
This class creates the whole level at once segments of which are displayed during gameplay.

####People:
The People class has all the variables and functionality of Mario, this includes the movement and collision checking.

####Enemies:
The Enemy class has all the variables and functionality of Mario, this includes the movement and collision checking.

####BossEnemy:
The BossEnemy class has all the variables and functionality of Mario, this includes the movement and collision checking. 

####Scoreboard:
Scoreboard class manages score, printing, and the killing of Mario.

__________________

How To Play:
------------------
>- Run the following code to start the game.
```
python3 main.py
```
>- 'w, a, d' use these controls for jump, left,and right.
>-  press 'q' to quit.

___________________

Reqiurements:
--------------------
- Python3
- NumPy