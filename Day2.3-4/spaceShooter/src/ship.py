import pygame

class Ship:

    def __init__(self, WINDOWWIDTH, WINDOWHEIGHT):
        self.imagelocation = r"C:\Users\William Lu\OneDrive\文档\StanfordOnline_GameDesign\game-design-course-code\Day2.3-4\spaceShooter\src\ArtAssets7\ship.png"
        self.image = pygame.transform.scale(pygame.image.load(self.imagelocation), (80,80))
        self.rect = self.image.get_rect()
        self.leftLimit = 10
        self.rightLimit = WINDOWWIDTH - 10
        self.upLimit = 10
        self.downLimit = WINDOWHEIGHT - 10
        self.moveSpeed = 5 #pixels per frame
        self.setStartPos()
        

    @property
    def rects(self):
        return [self.__rect1, self.__rect2]
    

    def move(self, left, right, up, down):
        if left and self.rect.left > self.leftLimit:
            self.rect.left -= self.moveSpeed
            self.rects[0].left -= self.moveSpeed
            self.rects[1].left -= self.moveSpeed
        if right and self.rect.right < self.rightLimit:
            self.rect.right += self.moveSpeed
            self.rects[0].right += self.moveSpeed
            self.rects[1].right += self.moveSpeed
        if up and self.rect.top > self.upLimit:
            self.rect.top -= self.moveSpeed
            self.rects[0].top -= self.moveSpeed
            self.rects[1].top -= self.moveSpeed
        if down and self.rect.bottom < self.downLimit:
            self.rect.bottom += self.moveSpeed
            self.rects[0].bottom += self.moveSpeed
            self.rects[1].bottom += self.moveSpeed


    def setStartPos(self):
        # spawn the ship in the start position use ship center
        xCoord = (self.rightLimit + self.leftLimit) / 2
        yCoord = self.downLimit - self.rect.height / 2

        self.rect.center = (xCoord, yCoord)

        self.__rect1 = pygame.Rect(self.rect.left, self.rect.top+40, 80, 30)
        self.__rect2 = pygame.Rect(self.rect.left+25, self.rect.top, 30, 80)


    def colliderect(self, otherRect):
        for rect in self.rects:
            if rect.colliderect(otherRect):
                return True
        return False