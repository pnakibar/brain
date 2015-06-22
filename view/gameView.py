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
                        self.gameController.rodaTurno()
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
        self.font = pygame.font.Font(None, 72)
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
                text = self.create_text("Voce perdeu!", (128, 0, 0))        
                self.display.blit(text, (0,0))
                pass

        pygame.display.flip()
        pygame.display.update()

    def run(self):
        self.initDisplay()
        while(True):
            self.eventHandler()
            self.updateDisplay()