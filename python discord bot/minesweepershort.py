import os
import sys

#add minesweeper.py to the path
pathstring = "C:/Users/Owner/Downloads/python discord bot/minesweeper.py"
sys.path.append(os.path.abspath(pathstring))
import minesweeper
#import numpy as np
#import random

#X and Y are flipped 
mboard = minesweeper.generateboard(9,9,9)
print(mboard)

#print(minesweeper.boardtoemoji(mboard))

