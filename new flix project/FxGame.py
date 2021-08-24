import pygame
from pygame.locals import *
import sys
# so we can read paths and gameinfo
import json
# do it urself idk how to :(
import pypresence
def gameStart():
  # do something here
  pass

#game setup noncence
with open('gameinfo.json') as gameinfo:
  data = json.load(gameinfo)
with open('assets.json') as assetpath:
  assetPaths = json.load(assetpath)

def initGame(r:float, g:float, b:float, width, hight):
    createdgame = pygame.init()
    # varibles go here..
    size = width, height = width, hight
    screen = pygame.display.set_mode(size)
    color = r, g, b
    screen.fill(color)
    gameName = data.get('name')
    gameVer = data.get('version')
    pygame.display.set_caption(gameName)
    print("game " + gameName + " version " + str(gameVer) + " created!")
    return(createdgame)

# the numbers are rgb values they are the backround color
initGame(0, 0, 0, 640, 480)
# run the start function
gameStart()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

def quitGame():
    sys.exit()

# put ur code here now :)
print("running users code")


