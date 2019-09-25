import splendor_cards as cards
import splendor_nobles as nobles
import splendor_player as player
import random

red, green, blue, white, black, yellow = 'red', 'green', 'blue', 'white', 'black', 'yellow'


deck1 = cards.deckLVL1.copy()

random.shuffle(deck1)

card1 = deck1[0]
card2 = deck1[1]
card3 = deck1[2]
card4 = deck1[3]

player1 = player.player('Toby')

player1.addToken(red, 5)



def purchaseCard(player, card):
    cardRequirements = card.easyRequirements
    playerTokens = player.tokens

    for color in cardRequirements.keys():
        cardColorRequirement = cardRequirements[color]
        playerColorCount = playerTokens[color]

        if cardColorRequirement > playerColorCount:
            return False, player
        else:
            player.tokens[color] - card.easyRequirements[color]
    player.addCard(card)
    return True, player

