import pygame, sys
import random as r
from pygame.locals import *

from Circle import Circle
def _bounce_the_wall(self):
    if self.center[0] <= self.radius or self.center[0] >= RESOLUTION[0]-self.radius-5:
        self.velocity[0] *= -1
    
    if self.center[1] <= self.radius or self.center[1] >= RESOLUTION[1]-self.radius-5:
        self.velocity[1] *= -1
Circle.bounce_the_wall = _bounce_the_wall

def _draw(self):
        pygame.draw.circle(DISPLAYSURF, self.color, self.center, self.radius)
Circle.draw = _draw


pygame.init()
RESOLUTION = (500, 500)
DISPLAYSURF = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption("Bouncing Balls")
FPS = 30
fpsClock = pygame.time.Clock()


ball1 = Circle([40, 40], 30, (255, 0, 0))
ball2 = Circle([300, 50], 40, (0, 0, 255))
ball3 = Circle([30, 300], 20, (0, 255, 0))
ball4 = Circle([300, 300], 20, (128, 0, 128))
ball5 = Circle([100, 350], 25, (128, 128, 0))
ball6 = Circle([50, 450], 20, (0, 128, 128))
balls = [ball1, ball2, ball3, ball4, ball5, ball6]

while True:
    DISPLAYSURF.fill((255, 255, 255))

    for ball in balls:
        for another_ball in balls:
            if not another_ball == ball:
                ball.bounce_the_ball(another_ball)
        ball.bounce_the_wall()
        ball.move()
        ball.draw()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    fpsClock.tick(FPS)
