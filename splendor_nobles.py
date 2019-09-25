import nobleLibrary

class noble():
    def __init__(self, name, requirements):
        self.name = name # Each patron receives a designation/name
        self.pointValue = 3 # The patron's value towards player score. It's always 3.
        self.requirements = requirements # The patron's card requirements, as a tuple.
    
    def __repr__(self):
        return(f"noble('{self.name}', '{self.requirements}')")

    def __str__(self):
        return(f'{self.name}')

#statics:
# colours

red, green, blue, white, black, yellow = 'red', 'green', 'blue', 'white', 'black', 'yellow'


noblesDeck = [noble(person[0], person[1]) for person in nobleLibrary.nobles.items()]


