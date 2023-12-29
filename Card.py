class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def getSuit(self):
        return self.suit

    def getValue(self):
        print("card getValue method - remove this print statement when you add your code")
        return self.value

    def __str__(self):
        return f"{self.value}{self.suit}"
