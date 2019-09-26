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





deck1RawData = cardLibrary.cardsInDeckLv1
deck2RawData = cardLibrary.cardsInDeckLv2
deck3RawData = cardLibrary.cardsInDeckLv3


deckLVL1 = []
for cardColour in deck1RawData.keys():
    for cardData in deck1RawData[cardColour].values():
        asCardObject = card(cardColour, cardData['requirements'], cardData['points'])
        deckLVL1.append(asCardObject)

deckLVL2 = []
for cardColour in deck2RawData.keys():
    for cardData in deck2RawData[cardColour].values():
        asCardObject = card(cardColour, cardData['requirements'], cardData['points'])
        deckLVL2.append(asCardObject)

deckLVL3 = []
for cardColour in deck3RawData.keys():
    for cardData in deck3RawData[cardColour].values():
        asCardObject = card(cardColour, cardData['requirements'], cardData['points'])
        deckLVL3.append(asCardObject)










