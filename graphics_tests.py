red, green, blue, white, black, yellow = 'red', 'green', 'blue', 'white', 'black', 'yellow'


import random, time, sys
import pygame
from pygame.locals import *
from splendor_gameUtils import *


tableTokens = {
    red:3,
    green:3,
    blue:3,
    white:3,
    black:3,
    yellow:3
}


redTokenSurf = pygame.Surface((60,70), pygame.SRCALPHA)
redTokenRect = redTokenSurf.get_rect()
redTokenRect.topleft = (100,100)

redTokenSurf.fill(NOCOLOUR)


def drawTokens(asurface, tokens):
    redTokens = tokens[red]
    greenTokens = tokens[green]
    blueTokens = tokens[blue]
    whiteTokens = tokens[white]
    blackTokens = tokens[black]


    if redTokens:
        
        for token in range(redTokens):
            baseYPos = 40
            tokenYPos = baseYPos - (3*token)
            
            pygame.draw.circle(redTokenSurf, LIGHTRED, (30,tokenYPos), 30)
            pygame.draw.circle(redTokenSurf, RED, (30,tokenYPos), 30, 1)
            # pygame.draw.circle(asurface, BLACK, (100,tokenYPos), 30, 2)

        asurface.blit(redTokenSurf, redTokenRect)

    if greenTokens:
        for token in range(greenTokens):
            baseYPos = 100
            tokenYPos = baseYPos - (3*token)
            
            pygame.draw.circle(asurface, LIGHTGREEN, (200,tokenYPos), 30)
            pygame.draw.circle(asurface, GREEN, (200,tokenYPos), 30, 1)
            # pygame.draw.circle(asurface, BLACK, (100,tokenYPos), 30, 2)
def drawTokenAtMouse(x,y, color, asurface):
    movingTokenSurf = pygame.Surface((60, 60), pygame.SRCALPHA)
    # movingTokensurf = movingTokenSurf.convert_alpha()
    # movingTokenSurf.fill(NOCOLOUR)
    movingTokenRect = movingTokenSurf.get_rect()
    movingTokenRect.center = (x, y)
    if color == red:
        highlight = LIGHTRED
        shade = RED    

    pygame.draw.circle(movingTokenSurf, highlight, (30,30), 30)
    pygame.draw.circle(movingTokenSurf, shade, (30,30), 30, 1)
    asurface.blit(movingTokenSurf, movingTokenRect)


def getTokenClicked(x,y):
    
    if redTokenRect.collidepoint(x, y):
        print('Clicked RED')
        return red
    else:
        return None


def main():
    global redTokenSurf
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('SPLENDOR')

    mouseDown = False
    tokenClicked = None
    while True:
        checkForQuit()
        DISPLAYSURF.fill(GRAY)

        drawTokens(DISPLAYSURF, tableTokens)


        
        
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos

            if event.type == MOUSEBUTTONDOWN:
                mouseDown = True
                mousex, mousey = event.pos
                tokenClicked = getTokenClicked(mousex, mousey)
                
            if event.type == MOUSEBUTTONUP:
                mouseDown = False
                tokenClicked = None

        if mouseDown and tokenClicked:
            drawTokenAtMouse(mousex, mousey, tokenClicked, DISPLAYSURF)

        pygame.display.update()
        
        FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    main()