import pygame
from FxGame import Game
from FxTools import FxTools
from pygame.locals import *
import sys
# so we can read paths and gameinfo
import json
# do it urself idk how to :(
import pypresence
import os 

class main:
    gae = Game.initialised()
    gae = Game.initGame(0, 0, 0, 640, 480)
    def __init__(self):
        pass #ran when game is loaded
    while 1:
        Game.updateKeybinds()