red, green, blue, white, black, yellow = 'red', 'green', 'blue', 'white', 'black', 'yellow'


import random, time, sys
import pygame
from pygame.locals import *
from splendor_gameUtils import *



def drawTableTokens(asurface, tokens):
    redTokens = tokens[red]
    greenTokens = tokens[green]
    blueTokens = tokens[blue]
    whiteTokens = tokens[white]
    blackTokens = tokens[black]
    
    if redTokens:
        tableRedTokenSurf.fill(NOCOLOUR)     
        
        for token in range(redTokens):
            baseYPos = 50
            tokenYPos = baseYPos - (3*token)
            
            pygame.draw.circle(tableRedTokenSurf, LIGHTRED, (30,tokenYPos), 30)
            pygame.draw.circle(tableRedTokenSurf, RED, (30,tokenYPos), 30, 1)
            # pygame.draw.circle(asurface, BLACK, (100,tokenYPos), 30, 2)

        asurface.blit(tableRedTokenSurf, tableRedTokenRect)

    if greenTokens:
        tableGreenTokenSurf.fill(NOCOLOUR)
        for token in range(greenTokens):

            baseYPos = 50
            tokenYPos = baseYPos - (3*token)
            
            pygame.draw.circle(tableGreenTokenSurf, LIGHTGREEN, (30,tokenYPos), 30)
            pygame.draw.circle(tableGreenTokenSurf, GREEN, (30,tokenYPos), 30, 1)
            # pygame.draw.circle(asurface, BLACK, (100,tokenYPos), 30, 2)
        asurface.blit(tableGreenTokenSurf, tableGreenTokenRect)

def drawPlayerTokens(asurface, tokens):
    redTokens = tokens[red]
    greenTokens = tokens[green]
    blueTokens = tokens[blue]
    whiteTokens = tokens[white]
    blackTokens = tokens[black]
    
    if redTokens:
        playerRedTokenSurf.fill(NOCOLOUR)     
        
        for token in range(redTokens):
            baseYPos = 50
            tokenYPos = baseYPos - (3*token)
            
            pygame.draw.circle(playerRedTokenSurf, LIGHTRED, (30,tokenYPos), 30)
            pygame.draw.circle(playerRedTokenSurf, RED, (30,tokenYPos), 30, 1)
            # pygame.draw.circle(asurface, BLACK, (100,tokenYPos), 30, 2)

        asurface.blit(playerRedTokenSurf, playerRedTokenRect)

    if greenTokens:
        playerGreenTokenSurf.fill(NOCOLOUR)
        for token in range(greenTokens):

            baseYPos = 50
            tokenYPos = baseYPos - (3*token)
            
            pygame.draw.circle(playerGreenTokenSurf, LIGHTGREEN, (30,tokenYPos), 30)
            pygame.draw.circle(playerGreenTokenSurf, GREEN, (30,tokenYPos), 30, 1)
            # pygame.draw.circle(asurface, BLACK, (100,tokenYPos), 30, 2)
        asurface.blit(playerGreenTokenSurf, playerGreenTokenRect)

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
    
    if tableRedTokenRect.collidepoint(x, y):
        print('Clicked RED')
        tokens[red] -= 1
        print(f'There are now {tokens[red]} red tokens left.')
        return red, tokens
    elif tableGreenTokenRect.collidepoint(x, y):
        print('Clicked GREEN')
        tokens[green] -= 1
        print(f'There are now {tokens[green]} green tokens left.')
        return green, tokens
    
    else:
        return None, tokens


def main():
    global tableRedTokenSurf, tableRedTokenRect, tableGreenTokenSurf, tableGreenTokenRect
    global playerRedTokenSurf, playerRedTokenRect, playerGreenTokenSurf, playerGreenTokenRect
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

    playerTokens = {
        red:1,
        green:1,
        blue:1,
        white:1,
        black:1,
        yellow:1
    }

    tableRedTokenSurf = pygame.Surface((60,80), pygame.SRCALPHA)
    tableRedTokenSurf.fill(NOCOLOUR)
    tableRedTokenRect = tableRedTokenSurf.get_rect()
    tableRedTokenRect.topleft = (100,100)

    tableGreenTokenSurf = pygame.Surface((60,80), pygame.SRCALPHA)
    tableGreenTokenSurf.fill(NOCOLOUR)
    tableGreenTokenRect = tableGreenTokenSurf.get_rect()
    tableGreenTokenRect.topleft = (200,100)

    playerRedTokenSurf = pygame.Surface((60,80), pygame.SRCALPHA)
    playerRedTokenSurf.fill(NOCOLOUR)
    playerRedTokenRect = playerRedTokenSurf.get_rect()
    playerRedTokenRect.topleft = (WINDOWWIDTH-260,300)

    playerGreenTokenSurf = pygame.Surface((60,80), pygame.SRCALPHA)
    playerGreenTokenSurf.fill(NOCOLOUR)
    playerGreenTokenRect = playerGreenTokenSurf.get_rect()
    playerGreenTokenRect.topleft = (WINDOWWIDTH-160,300)     

    mouseDown = False
    tokenClicked = None
    while True:
        checkForQuit()
        DISPLAYSURF.fill(GRAY)

        drawTableTokens(DISPLAYSURF, tableTokens)
        drawPlayerTokens(DISPLAYSURF, playerTokens)


        
        
        for event in pygame.event.get(): # event handling loop
            if event.type == MOUSEMOTION:
                mousex, mousey = event.pos


            if event.type == MOUSEBUTTONDOWN:
                mouseDown = True
                mousex, mousey = event.pos
                tokenClicked, tableTokens = getTokenClicked(mousex, mousey, tableTokens)
                
            if event.type == MOUSEBUTTONUP:
                mouseDown = False
                if tokenClicked:
                    print('Momentarily, a token is in possession.')
                    
                tokenClicked = None

        if mouseDown and tokenClicked:
            drawTokenAtMouse(mousex, mousey, tokenClicked, DISPLAYSURF)

        pygame.display.update()
        
        FPSCLOCK.tick(FPS)

if __name__ == "__main__":
    main()