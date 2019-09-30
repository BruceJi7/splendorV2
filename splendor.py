import splendor_cards as cards
import splendor_nobles as nobles
import splendor_player as player
import splendor_common as table
import random

red, green, blue, white, black, yellow = 'red', 'green', 'blue', 'white', 'black', 'yellow'


deck1 = cards.deckLVL1.copy()
deck2 = cards.deckLVL2.copy()
deck3 = cards.deckLVL3.copy()


random.shuffle(deck1)
random.shuffle(deck2)
random.shuffle(deck3)

tableTokens = table.setTableTokens(2)

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
    playerTokens = player.tokens

    for color in cardRequirements.keys():
        cardColorRequirement = cardRequirements[color]
        playerColorCount = playerTokens[color]

        if cardColorRequirement > playerColorCount:
            return False
    return True        

def purchaseCard(player, card, tableTokens, faceUpCards, sourceDeck):
    if isCardPurchasePossible(player, card):
        for color in card.easyRequirements.keys(): #Take the tokens from the player
            player.tokens[color] -= card.easyRequirements[color]
            tableTokens[color] += card.easyRequirements[color] #Return tokens to table
        player.addCard(card) #Give card to player
    
    faceUpCards, sourceDeck = table.replaceFaceUpCard(card, faceUpCards, sourceDeck)

    return player, tableTokens, faceUpCards, sourceDeck

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

#Testing the player picking up tokens functions

# print('The player currently has:')
# print(player1.tokens)
# player1, tableTokens = table.pickUpTokens(player1, tableTokens, red, red)
# print('The player now has:')
# print(player1.tokens)
# print('And there are now the following tokens on the table:')
# print(tableTokens)