import splendor_cards as cards
import splendor_nobles as nobles
import splendor_player as player
import splendor_common as table
import random
import pygame
from pygame.locals import *


red, green, blue, white, black, yellow = 'red', 'green', 'blue', 'white', 'black', 'yellow'


deck1 = cards.deckLVL1.copy()
deck2 = cards.deckLVL2.copy()
deck3 = cards.deckLVL3.copy()

# Shuffle main decks
random.shuffle(deck1)
random.shuffle(deck2)
random.shuffle(deck3)

# Set tokens on table, for 2 players
tableTokens = table.setTableTokens(2)


# Set 3 nobles on the table
noblesDeck = nobles.noblesDeck
random.shuffle(noblesDeck)
tableNobles = noblesDeck[0:3]


player1 = player.player('Toby')
player1Score = player1.getPrestige()


### Game Mechanic Functions ###

def printCards(deck):
    for card in deck:
        print(f'\t{card}')

def printTokens(tokenSet):
    for color in tokenSet.keys():
        print(f'There are {tokenSet[color]} {color} tokens on the table.')

def isCardPurchasePossible(player, card):
    cardRequirements = card.easyRequirements
    playerTokens = player.getCombinedWallet()

    for color in cardRequirements.keys():
        cardColorRequirement = cardRequirements[color]
        playerColorCount = playerTokens[color]

        if cardColorRequirement > playerColorCount:
            return False
    return True        

def purchaseCard(player, card, tableTokens, faceUpCards, sourceDeck):
    if isCardPurchasePossible(player, card):
        for color in card.easyRequirements.keys(): #Take the tokens from the player
            tokensToTake = card.easyRequirements[color] - player.getCardCount()[color]
            if tokensToTake <= 0:
                print(f'The player has enough cards to cover the {color} cost.')
                continue
            else:
                player.tokens[color] -= tokensToTake
                tableTokens[color] += tokensToTake #Return tokens to table
        player.addCard(card) #Give card to player
    
    faceUpCards, sourceDeck = table.replaceFaceUpCard(card, faceUpCards, sourceDeck)

    return player, tableTokens, faceUpCards, sourceDeck

def canCollectNoble(player, aNoble):
    playerCards = player.getCardCount()
    nobleRequirements = aNoble.requirements
    for color in nobleRequirements.keys():
        if nobleRequirements[color] > playerCards[color]:
            return False

    print(f'{player.name} wins the favour of {aNoble.name}')    
    return True

def collectNoble(player, noblesDeck):
    favoringNobles = []
    if noblesDeck:
        for noble in noblesDeck:
            if canCollectNoble(player, noble):
                favoringNobles.append(noble)
        if favoringNobles:
            if len(favoringNobles) == 1:
                print(f'{player.name} has gained the favour of {favoringNobles[0].name}!')
                player.addNoble(favoringNobles[0])
                noblesDeck.pop(0)
                return player, noblesDeck
            elif len(favoringNobles) > 1:
                nobleNames = [noble.name for noble in favoringNobles]
                print('You have gained the favour of multiple nobles!')
                print('They are:')
                for nobleName in nobleNames:
                    print(nobleName)
                print('You may only accept the favour of one noble at a time.')
                print('Enter the number of the noble you want to accept this turn.')
                for number, noble in enumerate(nobleNames):
                    print(f'{number+1}: {noble}')
                selectedNoble = int(input('...')) -1
                print(f'And so {favoringNobles[selectedNoble].name} gives you their favour this turn.')
                player.addNoble(favoringNobles[selectedNoble])
                noblesDeck.pop(selectedNoble)
                return player, noblesDeck
        else:
            print('You must gain more reknown before the nobles will favour you.')
            return player, noblesDeck
    else:
        print('The nobles are all spoken for.')


### PYGAME FUNCTIONS ###

# # Demo game loop:
# print('Setting the table...')

# faceUpLv1Cards, tableDeck1 = table.setFaceUpCards(deck1)
# faceUpLv2Cards, tableDeck2 = table.setFaceUpCards(deck2)
# faceUpLv3Cards, tableDeck3 = table.setFaceUpCards(deck3)
# print('The nobles on the table are:')
# for noble in tableNobles:
#     print(f'\t{noble}')

# while player1Score < 15:
#     roundCounter = 1
#     print('-'*100)
#     print(f'It is round {roundCounter}.\n')
#     printTokens(tableTokens)
#     print('The cards on the table are as follows:')
#     print('The level 1 cards available are:')
#     printCards(faceUpLv1Cards)
#     print('The level 2 cards available are:')
#     printCards(faceUpLv2Cards)
#     print('And the level 3 cards available are:')
#     printCards(faceUpLv3Cards)
    












