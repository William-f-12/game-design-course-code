import pygame

class Laser:

    def __init__(self, shipRect, speed, up=True):
        self.up = up
        self.imagelocation = r"C:\Users\William Lu\OneDrive\文档\StanfordOnline_GameDesign\game-design-course-code\Day2.3-4\spaceShooter\src\ArtAssets7\laser.png"
        self.image = pygame.image.load(self.imagelocation)
        self.__rect = self.image.get_rect()
        if self.up:
            self.__rect.midbottom = shipRect.midtop
        else:
            self.__rect.midtop = shipRect.midbottom
        self.speed = speed
        self.rect = pygame.Rect(self.__rect.left+20, self.__rect.top, self.__rect.width-40, self.__rect.height)

    
    @property
    def imageRect(self):
        return self.__rect

    
    def move(self):
        if self.up:
            self.rect.bottom -= self.speed
            self.__rect.bottom -= self.speed
        else:
            self.rect.bottom += self.speed
            self.__rect.bottom += self.speed