import pygame
import sys
from pygame.locals import *
from control.gameControl import *


class Screen:
    def __init__(self, gameController):
        self.floorTile = pygame.image.load("brain/assets/chao.png")
        self.gatoTile = pygame.image.load("brain/assets/gato.png")
        self.ratoTile = pygame.image.load("brain/assets/rato.png")
        self.backgroundTile = pygame.image.load("brain/assets/wall.png")
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


    def run(self):
        pygame.init()
        self.display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0, 32)

        while(True):

            self.display.fill(self.bgColor)
            self.drawLabirinto()
            self.drawActors()
            pygame.display.flip()
            pygame.display.update()

            if self.gameController.acabouJogo:
                if self.gameController.ratoVivo:
                    #TODO something nice
                    pass
                else:
                    #TODO something bad
                    pass

            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        if not self.gameController.acabouJogo:
                            self.gameController.rodaTurno()
                            break
                    elif event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
