import pygame
import sys
from pygame.locals import *
from control.gameControl import *


class Screen:
    def __init__(self, gameController):
        self.floorTile = pygame.image.load("assets/chao.png")
        self.gatoTile = pygame.image.load("assets/gato.png")
        self.ratoTile = pygame.image.load("assets/rato.png")
        self.backgroundTile = pygame.image.load("assets/wall.png")
        self.tileSize = 64

        self.gameController = gameController
        self.SCREEN_WIDTH = len(gameController.labirinto.labirinto[0]) * self.tileSize
        self.SCREEN_HEIGHT = len(gameController.labirinto.labirinto) * self.tileSize
        self.display = None
        self.__FPS = 60
        self.event = 0
        self.__end = True
        self.bgColor = (10, 166, 201)
	self.routeTile = colorize(self.floorTile, (0 , 0, 255))
	self.endTile = colorize(self.floorTile, (255 , 0, 0))
	self.startTile = colorize(self.floorTile, (0 , 255, 0))

	#favicon
	pygame.display.set_icon(self.ratoTile)

	#window name
	pygame.display.set_caption("BRAIN")


    def convertXYIntoRelativePosition(self, pos):
        x, y = pos
        newX = x*self.tileSize
        newY = y*self.tileSize
        return (newX, newY)


    def drawLabirinto(self):
        posY = 0
        posX = 0
        for y in self.gameController.getLabirinto():
            for x in y:
                if x != '0':
			if x == 'F':
				self.display.blit(self.endTile, (posX, posY))
			elif (posX/self.tileSize, posY/self.tileSize) in  self.gameController.rota: #HACK
				self.display.blit(self.routeTile, (posX, posY))
			elif x == 'S':
				self.display.blit(self.startTile, (posX, posY))
			
			else:
				self.display.blit(self.floorTile, (posX,posY))
                else:
			self.display.blit(self.backgroundTile, (posX,posY))
                posX = posX + self.tileSize
            posY = posY + self.tileSize
            posX = 0

    def drawActors(self):
        gatoX, gatoY = self.convertXYIntoRelativePosition(self.gameController.getGatoPos())
        ratoX, ratoY = self.convertXYIntoRelativePosition(self.gameController.getRatoPos())
        self.display.blit(self.gatoTile, (gatoX,gatoY))
        self.display.blit(self.ratoTile, (ratoX,ratoY))

    def eventHandler(self):
        def quit():
            pygame.quit()
            sys.exit()
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    if not self.gameController.acabouJogo:
                        try:
                            self.gameController.rodaTurno()
                        except Exception:
                            self.error = True
                        break
                    else:
                        quit()

                elif event.key == K_ESCAPE:
                    quit()

    def create_text(self, text, color):
        image = self.font.render(text, True, color)
        return image

    def initDisplay(self):
        pygame.init()
        self.fontSize = 32 
        self.font = pygame.font.Font(None, self.fontSize)
        self.display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0, 32)

    def updateDisplay(self):
        self.display.fill(self.bgColor)
        self.drawLabirinto()
        self.drawActors()

        if self.gameController.acabouJogo:
            if self.gameController.ratoVivo:
                text = self.create_text("Voce ganhou!", (0, 128, 0))        
                self.display.blit(text, (0,0))
            else:
                if self.error:
                    text = self.create_text("Nao da pra chegar no final!", (128, 0, 0))        
                else:
                    text = self.create_text("Voce perdeu!", (128, 0, 0))        
                self.display.blit(text, (0,0))
                pass

        pygame.display.flip()
        pygame.display.update()

    def run(self):
        self.error = False
        self.initDisplay()
        while(True):
            self.eventHandler()
            self.updateDisplay()

def colorize(image, newColor):
    """
    Create a "colorized" copy of a surface (replaces RGB values with the given color, preserving the per-pixel alphas of
    original).
    :param image: Surface to create a colorized copy of
    :param newColor: RGB color to use (original alpha values are preserved)
    :return: New colorized Surface instance
    """
    image = image.copy()

    # zero out RGB values
    # image.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    # add in new RGB values
    image.fill(newColor[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)

    return image
