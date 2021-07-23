import pygame, sys
import numpy as np
from pygame.locals import *

from ship import Ship
from enemyShip import EnemyShip
from laser import Laser
from asteroid import Asteroid
from background import Background

#Set up window and frame rate variables
FPS = 30
WINDOWWIDTH = 500
WINDOWHEIGHT = 700

#Set up some Color variables
RED = (255, 0, 0)
PINK = (200,100,100)
NAVYBLUE = (0, 0, 128)
WHITE = (255, 255, 255)

#Start the game
def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT #True globals
    
    pygame.init()
    
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption("Space Shooter")
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

    showStartScreen()
    while True:
        score, WinOrLose = runGame()
        showGameOverScreen(score, WinOrLose)


def runGame():
    # set up
    score = 0 # number of asteroids destroyed
    lives = 3
    levelUp = False

    # Create game object: ship asteroids ;asers background
    # ship controls
    playerShip = Ship(WINDOWWIDTH, WINDOWHEIGHT)
    leftHeld = False
    rightHeld = False
    upHeld = False
    downHeld = False
    firing = False

    # Lasers
    lasers = initializeObjects(10)
    laserIndex = 0
    laserSpeed = 10

    # Asteroid stuff
    asteroids = initializeObjects(25)
    spawnRate = 1 # per second, average
    minAsteroidSpeed = 1
    maxAsteroidSpeed = 6
    asteroidIndex = 0

    # background
    backgroundObject = Background("background", WINDOWHEIGHT)
    paralaxObject = Background("paralax", WINDOWHEIGHT)

    # enemy ship
    enemyShip = EnemyShip(WINDOWWIDTH, WINDOWHEIGHT)
    bossBattle = False
    e_lasers = initializeObjects(10)
    e_firing = False
    e_fireRate = 1.3
    e_laserIndex = 0

    # game loop
    while True:
        # event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                if event.key == K_a or event.key == K_LEFT:
                    leftHeld = True
                if event.key == K_d or event.key == K_RIGHT:
                    rightHeld = True
                if event.key == K_w or event.key == K_UP:
                    upHeld = True
                if event.key == K_s or event.key == K_DOWN:
                    downHeld = True
                if event.key == K_SPACE:
                    firing = True
            elif event.type == KEYUP:
                if event.key == K_a or event.key == K_LEFT:
                    leftHeld = False
                if event.key == K_d or event.key == K_RIGHT:
                    rightHeld = False
                if event.key == K_w or event.key == K_UP:
                    upHeld = False
                if event.key == K_s or event.key == K_DOWN:
                    downHeld = False
                if event.key == K_SPACE:
                    firing = False

        # increase game difficulty
        if score % 10 == 0 and levelUp and not bossBattle:
            minAsteroidSpeed += 2
            maxAsteroidSpeed += 2
            spawnRate += 0.7
            levelUp = False
        elif score % 10 != 0:
            levelUp = True

        # boss
        if score >= 100:
            bossBattle = True
            spawnRate = 0.7
        
        if bossBattle:
            # move
            enemyShip.enemyShipMove()
            if np.random.randint(0, FPS / e_fireRate) == 0:
                e_firing = True

        # spawn lasers
        if firing:
            lasers[laserIndex] = Laser(playerShip.rect, laserSpeed)
            laserIndex += 1
            firing = False
            if laserIndex >= len(lasers):
                laserIndex = 0
        if e_firing:
            e_lasers[e_laserIndex] = Laser(enemyShip.rect, laserSpeed, up=False)
            e_laserIndex += 1
            e_firing = False
            if e_laserIndex >= len(e_lasers):
                e_laserIndex = 0

        # automate asteroid spawning
        if np.random.randint(0, FPS / spawnRate) == 0:
            asteroids[asteroidIndex] = Asteroid(WINDOWWIDTH, WINDOWHEIGHT, np.random.randint(minAsteroidSpeed, maxAsteroidSpeed))
            asteroidIndex += 1
            if asteroidIndex >= len(asteroids):
                asteroidIndex = 0

        # update state
        playerShip.move(left=leftHeld, right=rightHeld, up=upHeld, down=downHeld)
        backgroundObject.move()
        paralaxObject.move()
        for laser in lasers:
            if laser != None:
                laser.move()
        for e_laser in e_lasers:
            if e_laser != None:
                e_laser.move()
        for asteroid in asteroids:
            if asteroid != None:
                asteroid.move()

        # detect collisions
        for currentAsteroidIndex, asteroid in enumerate(asteroids):
            if asteroid != None:
                for currentLaserIndex, laser in enumerate(lasers):
                    if laser != None:
                        if laser.rect.colliderect(asteroid.rect):
                            asteroids[currentAsteroidIndex] = None
                            lasers[currentLaserIndex] = None
                            score += 1
                if playerShip.colliderect(asteroid.rect):
                    lives -= 1
                    if lives > 0:
                        playerHit()
                        playerShip.setStartPos()
                        asteroids = initializeObjects(25)
                        lasers = initializeObjects(10)
                        e_lasers = initializeObjects(10)
                    else:
                        return score, "lose"
                    break
        
        if bossBattle:
            for e_laser in e_lasers:
                if e_laser != None:
                    if playerShip.colliderect(e_laser.rect):
                        lives -= 1
                        if lives > 0:
                            playerHit()
                            playerShip.setStartPos()
                            asteroids = initializeObjects(25)
                            lasers = initializeObjects(10)
                            e_lasers = initializeObjects(10)
                        else:
                            return score, "lose"
                        break

            for currentLaserIndex, laser in enumerate(lasers):
                if laser != None:
                    if enemyShip.colliderect(laser.rect):
                        lasers[currentLaserIndex] = None
                        enemyShip.hp -= 1
                        if enemyShip.hp == 0:
                            return score, "win"
                        break



        # draw on screen
        draw(backgroundObject.image, backgroundObject.rect)
        draw(paralaxObject.image, paralaxObject.rect)
        # pygame.draw.rect(DISPLAYSURF,WHITE,playerShip.rects[0])
        # pygame.draw.rect(DISPLAYSURF,WHITE,playerShip.rects[1])
        # pygame.draw.rect(DISPLAYSURF,WHITE,enemyShip.rects[0])
        # pygame.draw.rect(DISPLAYSURF,WHITE,enemyShip.rects[1])
        draw(playerShip.image, playerShip.rect) # args = image, rect
        if bossBattle:
            draw(enemyShip.image, enemyShip.rect)
            drawLasers(e_lasers)
        drawLasers(lasers)
        drawAsteroids(asteroids)

        drawHUD(lives, score, bossBattle, enemyShip.hp)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def drawHUD(lives, score, bossBattle, e_hp):
    healthBarSurf = BASICFONT.render("Ships remaining: "+str(lives), True, WHITE)
    healthBarRect = healthBarSurf.get_rect()
    healthBarRect.topleft = (10, 10)
    draw(healthBarSurf, healthBarRect)
    healthBar = pygame.Rect(10, 35, 190, 30)
    pygame.draw.rect(DISPLAYSURF, NAVYBLUE, healthBar)
    health = pygame.Rect(15, 40, 60*lives, 20)
    pygame.draw.rect(DISPLAYSURF, RED, health)

    scoreSurf = BASICFONT.render("Asteroids Destroyed: "+str(score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topright = (WINDOWWIDTH - 10, 10)
    draw(scoreSurf, scoreRect)

    if bossBattle:
        e_healthBarSurf = BASICFONT.render("Enemy HP: "+str(e_hp), True, WHITE)
        e_healthBarRect = e_healthBarSurf.get_rect()
        e_healthBarRect.topright = (WINDOWWIDTH - 10, 35)
        draw(e_healthBarSurf, e_healthBarRect)
        e_healthBar = pygame.Rect(WINDOWWIDTH - 200, 60, 190, 30)
        pygame.draw.rect(DISPLAYSURF, NAVYBLUE, e_healthBar)
        e_health = pygame.Rect(WINDOWWIDTH - 195, 65, 9*e_hp, 20)
        pygame.draw.rect(DISPLAYSURF, RED, e_health)


def playerHit():
    hitSurf = BASICFONT.render("You've been destroyed!", True, WHITE)
    hitRect = hitSurf.get_rect()
    hitRect.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
    draw(hitSurf, hitRect)

    pygame.display.update()
    pygame.time.wait(2000) # wait 2 second


def drawLasers(lasers):
    for laser in lasers:
        if laser != None:
            # pygame.draw.rect(DISPLAYSURF, PINK, laser.rect)
            draw(laser.image, laser.imageRect)


def drawAsteroids(asteroids):
    for asteroid in asteroids:
        if asteroid != None:
            image, rect = asteroid.draw()
            # pygame.draw.rect(DISPLAYSURF,DARKGRAY,rect)
            draw(image, rect)


def initializeObjects(number):
    objects = []
    for i in range(number):
        objects.append(None)
    return objects


def draw(imageSurf, imageRect):
    DISPLAYSURF.blit(imageSurf, imageRect)


def terminate():
    pygame.quit()
    sys.exit()


def showStartScreen():
    DISPLAYSURF.fill(NAVYBLUE)
    startSurf = BASICFONT.render("Space Shooter", True, WHITE)
    startRect = startSurf.get_rect()
    startRect.midtop = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
    DISPLAYSURF.blit(startSurf, startRect)
    pygame.display.update()
    pygame.time.wait(500)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    return


    
def showGameOverScreen(score, WinOrLose):
    DISPLAYSURF.fill(NAVYBLUE)
    OverSurf = BASICFONT.render("Game Over", True, WHITE)
    OverRect = OverSurf.get_rect()
    OverRect.midtop = (WINDOWWIDTH / 2, 300)
    DISPLAYSURF.blit(OverSurf, OverRect)
    ScoreSurf = BASICFONT.render("Score: "+str(score), True, WHITE)
    ScoreRect = ScoreSurf.get_rect()
    ScoreRect.midtop = (WINDOWWIDTH / 2, OverRect.bottom+50)
    DISPLAYSURF.blit(ScoreSurf, ScoreRect)
    WLSurf = BASICFONT.render(WinOrLose, True, WHITE)
    WLRect = WLSurf.get_rect()
    WLRect.midtop = (WINDOWWIDTH / 2, ScoreRect.bottom+50)
    DISPLAYSURF.blit(WLSurf, WLRect)
    pygame.display.update()
    pygame.time.wait(3000)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    return


if __name__ == '__main__':
    main()