import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "check window width or cellsize"
assert WINDOWHEIGHT % CELLSIZE == 0, "check window height or cellsize"
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

WHITE       = (255, 255, 255)
BLACK       = (0, 0, 0)
RED         = (255, 0, 0)
GREEN       = (0, 255, 0)
DARKGREEN   = (0, 155, 0)
DARKGRAY    = (40, 40, 40)
BLUE        = (0, 0, 255)
BGCOLOR = BLACK

UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

HEAD = 0

apple_list = ["normal", "speed", "slow", "double", "poison"]

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font("freesansbold.ttf", 18)
    pygame.display.set_caption("Wormy")

    showStartScreen()
    while True:
        runGame()
        showGameOverScreen()


def runGame():
    # spawn at arandom starting point
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    if startx > (CELLWIDTH / 2 ):
        direction = LEFT
    else:
        direction = RIGHT
    wormCoords = [{"x": startx, "y": starty},
                  {"x": startx-1, "y": starty},
                  {"x": startx-2, "y": starty},]
    speed = 125
    apple = getRandomApple()

    # Game loop(while)
    while True:
        # ecent handler
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        if not wormCoords:
            return

        # detect "collisions"
        # check if the worm his hit itself or wall
        if wormCoords[HEAD]["x"] == -1 or wormCoords[HEAD]["y"] == -1 or wormCoords[HEAD]["x"] == CELLWIDTH or wormCoords[HEAD]["y"] == CELLHEIGHT:
            return
        for wormBody in wormCoords[3:]:
            if wormBody["x"] == wormCoords[HEAD]["x"] and wormBody["y"] == wormCoords[HEAD]["y"]:
                return

        # check if the worm has eaten the apple
        if wormCoords[HEAD]["x"] == apple["x"] and wormCoords[HEAD]["y"] == apple["y"]:
            if apple["type"] == "normal":
                apple = getRandomApple()
            elif apple["type"] == "speed":
                speed -= 100
                speed = max(speed, 25)
                apple = getRandomApple()
            elif apple["type"] == "slow":
                speed += 100
                speed = min(speed, 225)
                apple = getRandomApple()
            elif apple["type"] == "double":
                if direction == UP:
                    apple = {"x": wormCoords[HEAD]["x"], "y": wormCoords[HEAD]["y"]-1, "type": "normal"}
                elif direction == DOWN:
                    apple = {"x": wormCoords[HEAD]["x"], "y": wormCoords[HEAD]["y"]+1, "type": "normal"}
                elif direction == LEFT:
                    apple = {"x": wormCoords[HEAD]["x"]-1, "y": wormCoords[HEAD]["y"], "type": "normal"}
                elif direction == RIGHT:
                    apple = {"x": wormCoords[HEAD]["x"]+1, "y": wormCoords[HEAD]["y"], "type": "normal"}
            elif apple["type"] == "poison":
                del wormCoords[-1]
                apple = getRandomApple()
        else:
            del wormCoords[-1]
        
        # move the worm
        if direction == UP:
            newHead = {"x": wormCoords[HEAD]["x"], "y": wormCoords[HEAD]["y"]-1}
        elif direction == DOWN:
            newHead = {"x": wormCoords[HEAD]["x"], "y": wormCoords[HEAD]["y"]+1}
        if direction == LEFT:
            newHead = {"x": wormCoords[HEAD]["x"]-1, "y": wormCoords[HEAD]["y"]}
        if direction == RIGHT:
            newHead = {"x": wormCoords[HEAD]["x"]+1, "y": wormCoords[HEAD]["y"]}

        wormCoords.insert(0, newHead)

        # last thing we do
        # paint on the screen
        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        GrawWorm(wormCoords)
        drawApple(apple)
        drawScore(len(wormCoords) - 3)
        pygame.display.update()
        pygame.time.wait(speed)


def getRandomApple():
    return {"x": random.randint(1, CELLWIDTH-2), "y": random.randint(1, CELLHEIGHT-2), "type": random.choice(apple_list)}


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE):
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


def GrawWorm(wormCoords):
    for segment in wormCoords:
        x = segment["x"] * CELLSIZE
        y = segment["y"] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, BLUE, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x+4, y+4, CELLSIZE-8, CELLSIZE-8)
        pygame.draw.rect(DISPLAYSURF, WHITE, wormInnerSegmentRect)


def drawApple(apple):
    x = apple["x"] * CELLSIZE
    y = apple["y"] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)


def drawScore(score):
    scoreSurf = BASICFONT.render(str(score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.top = 10
    scoreRect.left = 10
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def terminate():
    pygame.quit()
    sys.exit()


def showStartScreen():
    gameStartFont = pygame.font.Font("freesansbold.ttf", 140)
    startSurf = gameStartFont.render("Wormy!!!", True, WHITE)
    startRect = startSurf.get_rect()
    startRect.midtop = (WINDOWWIDTH / 2, 150)

    DISPLAYSURF.blit(startSurf, startRect)

    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear the event cache

    while True:
        if checkForKeyPress():
            pygame.event.get()
            return


def checkForKeyPress():
    for event in pygame.event.get():
        if event.type == QUIT:
            terminate()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                terminate()
            else:
                return True
    return False


def showGameOverScreen():
    gameOverFont = pygame.font.Font("freesansbold.ttf", 150)
    gameSurf = gameOverFont.render("Game", True, WHITE)
    overSurf = gameOverFont.render("Over", True, WHITE)
    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)

    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)

    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear the event cache

    while True:
        if checkForKeyPress():
            pygame.event.get()
            return


if __name__ == "__main__":
    main()