import splendor_cards as cards
import splendor_nobles as nobles
import splendor_player as player
import splendor_common as table
import random

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


#Prepare face up cards
faceUpLv1Cards, tableDeck1 = table.setFaceUpCards(deck1)


player1 = player.player('Toby')

player1.addToken(red, 5)
player1.addToken(green, 5)
player1.addToken(blue, 5)
player1.addToken(white, 5)
player1.addToken(black, 5)

def testPrintCards(deck):
    for card in deck:
        print(card)

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
                noblesDeck.pop(favoringNobles[0])
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
                selectedNoble = int(input('...') -1)
                player.addNoble(favoringNobles[selectedNoble])
                noblesDeck.pop(selectedNoble)
                return player, noblesDeck
        else:
            print('You must gain more reknown before the nobles will favour you.')
            return player, noblesDeck
    else:
        print('The nobles are all spoken for.')

# print(len(deck1))
# tableLv1Cards = setTableCards(deck1)
# print(len(deck1))
# print(tableLv1Cards)




# # Testing the player purchase cards functions:

print('The player has the following cards:')
print(player1.cards)
print('The player has the following tokens')
print(player1.tokens)
print('There are the following cards on the table:')
for number, card in enumerate(faceUpLv1Cards):
    print(f'\t{number}: {card}')
print('The player will now buy a card.')
player1, tableTokens, faceUpLv1Cards, tableDeck1 = purchaseCard(player1, faceUpLv1Cards[1], tableTokens, faceUpLv1Cards, tableDeck1)
print('The player now has the following cards:')
print(player1.cards)
print('And the following tokens.')
print(player1.tokens)
print('And now the face up cards are as follows:')
for number, card in enumerate(faceUpLv1Cards):
    print(f'\t{number}: {card}')

print("The player's card buying power is now:")
print(player1.getCardCount())
print("And the player's total buying power is now:")
print(player1.getCombinedWallet())
print(f'The player has {player1.getPrestige()} points now.')
print('Cheating a noble into the player inventory:')
player1.addNoble(tableNobles[1])
player1.addNoble(tableNobles[0])
print(player1.nobles)
print(player1.getPrestige())

#Testing the player picking up tokens functions

# print('The player currently has:')
# print(player1.tokens)
# player1, tableTokens = table.pickUpTokens(player1, tableTokens, red, red)
# print('The player now has:')
# print(player1.tokens)
# print('And there are now the following tokens on the table:')
# print(tableTokens)

# print('The nobles present in this game are:')
# for noble in tableNobles:
#     print(f'\t{noble.name}')