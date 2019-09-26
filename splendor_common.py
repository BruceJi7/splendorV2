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


def setFaceUpCards(inDeck):
    tableDeck = random.choices(inDeck, k=4)
    for card in tableDeck:
        try:
            inDeck.remove(card)
        except:
            print(f'Tried to remove card: {card}.')
            print(f'Result is faceUpCards: {len(tableDeck)}, and {len(inDeck)} cards remaining in the deck.')
    print(f'Table is set, {len(tableDeck)} cards face up, {len(inDeck)} cards remaining in the deck.')
    return tableDeck, inDeck

def replaceFaceUpCard(cardToRemove, faceUpCards, inDeck):
    faceUpCards.remove(cardToRemove)
    newCard = random.choice(inDeck)
    inDeck.remove(newCard)
    faceUpCards.append(newCard)
    return faceUpCards, inDeck




# Can the player pick up two of a colour?
def canPlayerPickUpTwo(color, tableTokens):
    if tableTokens[color] >= 4:
        return True
    else:
        return False


