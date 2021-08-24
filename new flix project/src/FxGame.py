import pygame
from FxTools import FxTools
from pygame.locals import *
import sys
# so we can read paths and gameinfo
import json
# do it urself idk how to :(
import pypresence
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
createdgame = pygame.init()
#game setup noncence
print(dir_path)
with open(dir_path + "\gameinfo.json") as gameinfo:
  data = json.load(gameinfo)
with open(dir_path + "/assets.json") as assetpath:
  assetPaths = json.load(assetpath)

def gameStart():
  #do stuff here
  pass

gameName = data.get('name')
gameVer = data.get('version')
screen = pygame.display.set_mode((400,400))
screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 18)

def initGame(r:float, g:float, b:float, width, hight):
    # varibles go here..
    screen = pygame.display.set_mode((400,400))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)
    size = width, height = width, hight
    screen = pygame.display.set_mode(size)
    color = r, g, b
    screen.fill(color)
    pygame.display.set_caption(gameName)
    print("game " + gameName + " version " + str(gameVer) + " created!")
    return(createdgame)
def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text
# the numbers are rgb values they are the backround color
# the first three are rgb the others is hight and width
initGame(0, 0, 0, 640, 480)
# run the start function
gameStart()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           print("game " + gameName + " quit")
           sys.exit()
    screen.fill((0, 0, 0))
    screen.blit(update_fps(), (10,0))
    clock.tick(60)
    pygame.display.update()
           

def quitGame():
    sys.exit()

# put ur code here now :)
print("running users code")

#this is the example project you can use all assets and stuff i guess

print('loading some sprites')



