# ignore all this stuffffff

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

def quitGame():
	print("game " + gameName + " quit")
	sys.exit()


class Game:
	def initialised():
		# wierd fix
		return(False)
	def initGame(r:float, g:float, b:float, width, hight):
		createdgame = pygame.init()
		# varibles go here..
		size = width, height = width, hight
		screen = pygame.display.set_mode(size)
		color = r, g, b
		screen.fill(color)
		pygame.display.set_caption(gameName)
		print("game " + gameName + " version " + str(gameVer) + " created!")
		return(True)
		

	def exitGame():
		quitGame()
	def updateKeybinds():
		# litrally makes no sense but works
		gae = Game.initialised()
		gae = True
		if gae == True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Game.exitGame()




