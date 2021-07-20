import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

RESOLUTION = (800, 600)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)

WHITE = (255, 255, 255)
beardManimg = pygame.image.load("../ArtAssets5/beardManSmall.png")
beardManRect = beardManimg.get_rect() 
direction = "right"
SPEED = 5 # pixels per frame

beardManimgRight = beardManimg
beardManimgLeft = pygame.transform.flip(beardManimg, True, False)
currentBeardman = beardManimgRight

while True:
    DISPLAYSURF.fill(WHITE)

    if direction == "right":
        beardManRect.left += SPEED
        if beardManRect.right >= 790:
            direction = "down"
    elif direction == "down":
        beardManRect.top += SPEED
        if beardManRect.bottom >= 590:
            direction = "left"
            currentBeardman = beardManimgLeft
    elif direction == "left":
        beardManRect.left -= SPEED
        if beardManRect.left <= 10:
            direction = "up"
    elif direction == "up":
        beardManRect.top -= SPEED
        if beardManRect.top <= 10:
            direction = "right"
            currentBeardman = beardManimgRight

    DISPLAYSURF.blit(currentBeardman, beardManRect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
