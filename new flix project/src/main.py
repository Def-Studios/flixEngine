import pygame
from FxGame import FxGame
from FxTools import FxTools
from pygame.locals import *
import sys
# so we can read paths and gameinfo
import json
# do it urself idk how to :(
import pypresence
import os 

class main:
    def __init__(self):
        # init the game and create the window
        FxGame.initGame(0, 0, 0, 640, 480)
    while 1:
        pass #called every frame