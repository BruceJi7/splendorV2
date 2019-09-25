import cardLibrary
import random


red, green, blue, white, black = 'red', 'green', 'blue', 'white', 'black'

class card():
    def __init__(self, color, requirements={}, pointValue=0,):
        self.color = color
        self.fullRequirements = requirements
        self.pointValue = pointValue
        self.easyRequirements = self.getSimpleRequirements()

    def __repr__(self):
        return (f'card({self.color}, {self.fullRequirements}, {self.pointValue})')

    def __str__(self):
        return (f'A {self.color} card, worth {self.pointValue} points, that requires {self.easyRequirements}')

    def getReqForColor(self, color):
        return self.fullRequirements[color]
    
    def getSimpleRequirements(self):
        nonZeroColours = {}
        for pair in self.fullRequirements.items():
            if pair[1] != 0:
                nonZeroColours[pair[0]] = pair[1]
        return nonZeroColours





cardsFromLibrary = cardLibrary.cardsInDeckLv1


deckLVL1 = []
for cardColour in cardsFromLibrary.keys():
    for cardData in cardsFromLibrary[cardColour].values():
        asCardObject = card(cardColour, cardData['requirements'], cardData['points'])
        deckLVL1.append(asCardObject)


for cardItem in deckLVL1:
    print(cardItem)






