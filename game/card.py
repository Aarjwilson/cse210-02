import random

class Card:

    def __init__(self): #Set Default values
        self.value = 0

    def DrawCard(self): #Draw a random card number between 1 and 13
        self.value = random.randrange(1,14)

