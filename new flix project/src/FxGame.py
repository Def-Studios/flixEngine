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
init = 0
class Game:
  with open(dir_path + "\gameinfo.json") as gameinfo:
    data = json.load(gameinfo)
  with open(dir_path + "/assets.json") as assetpath:
    assetPaths = json.load(assetpath)
  # ignore evrything from now on
  gameName = data.get('name')
  gameVer = data.get('version')

  def initGame(r:float, g:float, b:float, width, hight):

      with open(dir_path + "\gameinfo.json") as gameinfo:
        data = json.load(gameinfo)
      with open(dir_path + "/assets.json") as assetpath:
        assetPaths = json.load(assetpath)
      createdgame = pygame.init()
      gameName = data.get('name')
      gameVer = data.get('version')
      # varibles go here..
      pygame.init()
      screen = pygame.display.set_mode(width, hight)
      color = r, g, b
      screen.fill(color)
      pygame.display.set_caption(gameName)
      print("game " + gameName + " version " + str(gameVer) + " created!")
      init = 1



while 1:
  if init == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           print("game " + gameName + " quit")
           sys.exit()

           

def quitGame():
    sys.exit()



