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

# setFaceUpCards - initialise the face up cards for one deck. Select the first 4 cards from the shuffled deck, remove them, and add them to face up cards.
def setFaceUpCards(shuffledDeck):
    tableDeck = shuffledDeck[0:4]
    shuffledDeck = shuffledDeck[4:]
    # print(f'There are {len(tableDeck)} face up cards on the table and {len(shuffledDeck)} remaining cards in the deck.')
    
    return tableDeck, shuffledDeck



### Action functions

#replaceFaceUpCard - Given a specific card from the faceUpCards deck, remove it from the deck, and put a new card in that position.
def replaceFaceUpCard(cardToRemove, faceUpCards, inDeck):
    if inDeck:
        cardIndex = faceUpCards.index(cardToRemove)
        faceUpCards.remove(cardToRemove)
        newCard = inDeck.pop()
        faceUpCards.insert(cardIndex, newCard)
        print(f'A new card, {newCard}, has been added to the table.')
    else:
        print('The deck is empty; no more cards can be put on the table.')
    return faceUpCards, inDeck

def pickUpTokens(player, tableTokens, *args):
    playerPickupAllowance = player.getPickupQuant()
    if len(args) <= playerPickupAllowance:
        if len(args) == 3 and len(set(args)) == 1:
            print('You cannot pick up three tokens of the same colour')
            return player, tableTokens
        elif len(args) == 3 and len(set(args)) == 2:
            print('You cannot pick up three tokens if two tokens are the same colour')
            return player, tableTokens
        else:
            if len(args) == 2 and args[0] == args[1]:
                if canPlayerPickUpTwo(args[0], tableTokens):
                    player.addToken(args[0], 2)
                    tableTokens[args[0]] -= 2
                    print(f'You picked up two {args[0]} tokens.')
                    return player, tableTokens
                else:
                    print(f'There are not enough {args[0]} coloured tokens to pick up two.')
                    return player, tableTokens
            else:
                for color in args:
                    player.addToken(color, 1)
                    tableTokens[color] -= 1
                print(f'You picked up {args} tokens')
                return player, tableTokens
    else:
        print(f'You cannot pick up that many tokens. You have {player.getTotalTokens()} tokens already. You may pick up {playerPickupAllowance} token(s).')
        return player, tableTokens


# Can the player pick up two of a colour?
def canPlayerPickUpTwo(color, tableTokens):
    if tableTokens[color] >= 4:
        return True
    else:
        return False
