import random
from Card import Card


class Deck:

    def __init__(self):
        self.deck = self.generateDeck()
        self.shuffle()

    '''
    shuffles the deck of cards by making 150 random swaps
    '''

    def shuffle(self):

        # PSEUDOCODE FOR THIS METHOD
        # repeat the following (indented lines of code) 150 times:

        # declare a variable called index1 and assign it to a random integer between 0 and (the length of the deck of Cards - 1)
        # declare a variable called index2 and assign it to a random integer between 0 and (the length of the deck of Cards - 1)

        # declare a variable called temp and assign it to the element of the deck of Cards located at index1
        # set the element of the deck of Cards located at index1 to the element of the deck located at index2
        # set the element of the deck of Cards located at index2 to temp
        for _ in range(150):
            index1 = random.randint(0, len(self.deck) - 1)
            index2 = random.randint(0, len(self.deck) - 1)
            temp = self.deck[index1]
            self.deck[index1] = self.deck[index2]
            self.deck[index2] = temp

    '''
    generates a deck of un-shuffled cards
    '''

    def generateDeck(self):
        suits = ["♠","♣","♥","♦"]
        values = ["1","2","3","4","5","6","7","8","9","10","11","12","13"]
        deck = []
        for suit in suits:
            for value in values:
                deck.append(Card(suit,value))

        return deck


    '''
    draws a card from the deck and return a card object
    '''

    def drawCard(self):
        return self.deck.pop(0)

    '''
    returns the number of cards left in the deck as an int
    '''

    def cardsLeft(self):
        return len(self.deck)