red, green, blue, white, black, yellow = 'red', 'green', 'blue', 'white', 'black', 'yellow'


import random, time, sys
import pygame
from pygame.locals import *
from splendor_gameUtils import *



def drawTokens(asurface, tokens):
    redTokens = tokens[red]
    greenTokens = tokens[green]
    blueTokens = tokens[blue]
    whiteTokens = tokens[white]
    blackTokens = tokens[black]

    


    if redTokens:
        redTokenSurf.fill(BLACK)     
        
        for token in range(redTokens):
            baseYPos = 50
            tokenYPos = baseYPos - (3*token)
            
            pygame.draw.circle(redTokenSurf, LIGHTRED, (30,tokenYPos), 30)
            pygame.draw.circle(redTokenSurf, RED, (30,tokenYPos), 30, 1)
            # pygame.draw.circle(asurface, BLACK, (100,tokenYPos), 30, 2)

        asurface.blit(redTokenSurf, redTokenRect)

    if greenTokens:
        greenTokenSurf.fill(NOCOLOUR)
        for token in range(greenTokens):

            baseYPos = 50
            tokenYPos = baseYPos - (3*token)
            
            pygame.draw.circle(greenTokenSurf, LIGHTGREEN, (30,tokenYPos), 30)
            pygame.draw.circle(greenTokenSurf, GREEN, (30,tokenYPos), 30, 1)
            # pygame.draw.circle(asurface, BLACK, (100,tokenYPos), 30, 2)
        asurface.blit(greenTokenSurf, greenTokenRect)

def drawTokenAtMouse(x,y, color, asurface):
    movingTokenSurf = pygame.Surface((60, 60), pygame.SRCALPHA)
    # movingTokensurf = movingTokenSurf.convert_alpha()
    # movingTokenSurf.fill(NOCOLOUR)
    movingTokenRect = movingTokenSurf.get_rect()
    movingTokenRect.center = (x, y)
    if color == red:
        highlight = LIGHTRED
        shade = RED

    elif color == green:
        highlight = LIGHTGREEN
        shade = GREEN    

    pygame.draw.circle(movingTokenSurf, highlight, (30,30), 30)
    pygame.draw.circle(movingTokenSurf, shade, (30,30), 30, 1)
    asurface.blit(movingTokenSurf, movingTokenRect)


def getTokenClicked(x,y, tokens):
    
    if redTokenRect.collidepoint(x, y):
        print('Clicked RED')
        tokens[red] -= 1
        print(f'There are now {tokens[red]} red tokens left.')
        return red, tokens
    elif greenTokenRect.collidepoint(x, y):
        print('Clicked GREEN')
        tokens[green] -= 1
        print(f'There are now {tokens[green]} green tokens left.')
        return green, tokens
    
    else:
        return None, tokens


def main():
    global redTokenSurf, redTokenRect, greenTokenSurf, greenTokenRect
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('SPLENDOR')

    tableTokens = {
        red:6,
        green:3,
        blue:3,
        white:3,
        black:3,
        yellow:3
    }

    redTokenSurf = pygame.Surface((60,80), pygame.SRCALPHA)
    redTokenSurf.fill(NOCOLOUR)
    redTokenRect = redTokenSurf.get_rect()
    redTokenRect.topleft = (100,100)

    greenTokenSurf = pygame.Surface((60,80), pygame.SRCALPHA)
    greenTokenSurf.fill(NOCOLOUR)
    greenTokenRect = greenTokenSurf.get_rect()
    greenTokenRect.topleft = (200,100)     

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
                tokenClicked, tableTokens = getTokenClicked(mousex, mousey, tableTokens)
                
            if event.type == MOUSEBUTTONUP:
                mouseDown = False
                tokenClicked = None

        if mouseDown and tokenClicked:
            drawTokenAtMouse(mousex, mousey, tokenClicked, DISPLAYSURF)

        pygame.display.update()
        
        FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    main()