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

gae = Game.initialised()
gae = Game.initGame(0, 0, 0, 640, 480)

class main:
    def __init__(self):
        if gae == True:
            pass #ran when finished init
    while 1:
        Game.updateKeybinds()