import random


# At first, I will write functions I expect to need here:
red, green, blue, white, black, yellow = 'red', 'green', 'blue', 'white', 'black', 'yellow'


### Initialisation Functions

#setTableTokens - set the number of tokens based on how many players are playing.
def setTableTokens(playerCount):
    outTokenPile = {}
    colorList = [red, green, blue, white, black]
    for color in colorList:
        outTokenPile.setdefault(color, 4)
    if playerCount >4:
        offset = playerCount-4
        for color in outTokenPile.keys():
            color += offset
    outTokenPile[yellow] = 5
    return outTokenPile


def setFaceUpCards(shuffledDeck):
    tableDeck = shuffledDeck[0:4]
    shuffledDeck = shuffledDeck[4:]
    print(f'There are {len(tableDeck)} face up cards and {len(shuffledDeck)} shuffled cards.')
    
    return tableDeck, shuffledDeck

def replaceFaceUpCard(cardToRemove, faceUpCards, inDeck):
    cardIndex = faceUpCards.index(cardToRemove)
    faceUpCards.remove(cardToRemove)
    newCard = inDeck.pop()
    faceUpCards.insert(cardIndex, newCard)
    return faceUpCards, inDeck




# Can the player pick up two of a colour?
def canPlayerPickUpTwo(color, tableTokens):
    if tableTokens[color] >= 4:
        return True
    else:
        return False


