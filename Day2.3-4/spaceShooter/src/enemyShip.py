import pygame
from pygame.constants import WINDOWHIDDEN
from ship import Ship

class EnemyShip(Ship):

    def __init__(self, WINDOWWIDTH, WINDOWHEIGHT):
        super(EnemyShip, self).__init__(WINDOWWIDTH, WINDOWHEIGHT)
        self.downLimit = WINDOWHEIGHT / 2 + self.rect.height
        self.left = True
        self.right = False
        self.down = False
        self.downDistance = self.rect.bottom
        
        self.image = pygame.transform.rotate(self.image, 180)
        self.hp = 20


    @property
    def rects(self):
        return [self.__rect1, self.__rect2]


    def setStartPos(self):
        # spawn the ship in the start position use ship center
        xCoord = (self.rightLimit + self.leftLimit) / 2
        yCoord = -10

        self.rect.center = (xCoord, yCoord)

        self.__rect1 = pygame.Rect(self.rect.left, self.rect.top+10, 80, 30)
        self.__rect2 = pygame.Rect(self.rect.left+25, self.rect.top, 30, 80)


    def enemyShipMove(self):
        if self.rect.left == self.leftLimit:
            self.left = False
            self.down = True
        elif self.rect.right == self.rightLimit:
            self.right = False
            self.down = True
        if self.rect.top >= self.downDistance or self.rect.bottom >= self.downLimit:
            self.down = False
            if self.rect.right == self.rightLimit:
                self.left = True
            elif self.rect.left == self.leftLimit:
                self.right = True
            self.downDistance = self.rect.bottom
        
        self.move(left=self.left, right=self.right, up=False, down=self.down)
        