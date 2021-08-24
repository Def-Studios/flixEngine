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

#game setup noncence
print(dir_path)
with open(dir_path + "\gameinfo.json") as gameinfo:
  data = json.load(gameinfo)
with open(dir_path + "/assets.json") as assetpath:
  assetPaths = json.load(assetpath)

  gameName = data.get('name')
  gameVer = data.get('version')
  inti = "0"
class FxGame:
  def initGame(r:float, g:float, b:float, width, hight):
	    # varibles go here..
      pygame.init()
      inti = [1]
      size = (width, hight)
      screen = pygame.display.set_mode(size)
      color = r, g, b
      screen.fill(color)
      pygame.display.set_caption(gameName)
      print("game " + gameName + " version " + str(gameVer) + " created!")

while 1:
  if inti == "1":
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           print("game " + gameName + " quit")
           sys.exit()
           

def quitGame():
    sys.exit()

# put ur code here now :)
print("running users code")


