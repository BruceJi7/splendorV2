import splendor_cards as cards
import splendor_nobles as nobles
import splendor_player as player
import splendor_common as table
import random

red, green, blue, white, black, yellow = 'red', 'green', 'blue', 'white', 'black', 'yellow'


deck1 = cards.deckLVL1.copy()

random.shuffle(deck1)

tableCards = deck1[0:4]
tableTokens = table.setTableTokens(2)


player1 = player.player('Toby')

player1.addToken(red, 5)
player1.addToken(green, 5)
player1.addToken(blue, 5)
player1.addToken(white, 5)
player1.addToken(black, 5)

def setTableCards(deck):

    tableCards = []
    for _ in range(4):
        selectedCard = random.choice(deck)
        tableCards.append(selectedCard)
        deck.remove(selectedCard)
    return tableCards


def isCardPurchasePossible(player, card):
    cardRequirements = card.easyRequirements
    playerTokens = player.tokens

    for color in cardRequirements.keys():
        cardColorRequirement = cardRequirements[color]
        playerColorCount = playerTokens[color]

        if cardColorRequirement > playerColorCount:
            return False
    return True        

def purchaseCard(player, card, tableTokens):
    if isCardPurchasePossible(player, card):
        for color in card.easyRequirements.keys():
            player.tokens[color] -= card.easyRequirements[color]
            tableTokens[color] += card.easyRequirements[color]
        player.addCard(card)
    return player, tableTokens

# print(len(deck1))
# tableLv1Cards = setTableCards(deck1)
# print(len(deck1))
# print(tableLv1Cards)


print(player1.cards)
print(player1.tokens)
player1, tableTokens = purchaseCard(player1, tableCards[0], tableTokens)
print(player1.cards)
print(player1.tokens)
print(tableTokens)