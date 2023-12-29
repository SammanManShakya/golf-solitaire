from Deck import Deck

'''
Note: DO NOT MODIFY THIS FUNCTION. If your grid is not displaying properly, check your code first or contact us. 

displays a grid of cards arranged in 7x5 col/row formatted like this:
[   [row1, row2, row3...],  <-col1
    [row1, row2, row3...],  <-col2
    [row1, row2, row3...],  <-col3
    ...
]

params:
    grid - a 2D list in the format shown above
6
returns:
    None (output from this function is printed)

'''


def displayGrid(grid):
    # generate and display the index header for the grid
    headerStr = ""
    for row in range(7):
        headerStr += " \t" + str(row) + "\t "
    print(headerStr)
    print()

    # proces through each of the rows in reverse because we need to print top to bottom (ie last index to first)
    for row in range(4, -1, -1):

        # generate the full string for a row before printing it
        rowStr = "|\t"
        for col in range(7):
            # create an index offset so that cards are always aligned at the top
            offset = 5 - len(grid[col])
            rowIdx = row - offset

            # as long as the row index is valid, get the data for that particular card
            if (rowIdx >= 0):
                rowStr += str(grid[col][rowIdx]) + "\t|\t"

            # otherwise print an empty space
            else:
                rowStr += "  \t|\t"

        # print the completed row and a row separator
        print(rowStr)
        print()


'''
Initializes a grid of cards for golf solitaire

params:
    deck - an instance of the deck class to draw cards from

returns:
    a 2D list of card objects formatted in a 7x5 configuration for 7 columns and 5 rows
'''


def initGrid(deck):
    # Initialize an empty 7x5 grid
    grid = []                                     #  0  1  2  3  4  5  6
    for _ in range(7):                    #  grid = [[],[],[],[],[],[],[]]
        grid.append([])

    # Adding cards from deck
    for col in range(7):
        for row in range(5):
            # Remove a card from the deck and add it to the grid
            card = deck.drawCard()
            grid[col].append(card)

    return grid

'''
Checks whether the grid is empty (ie the grid is a list containing only empty lists). Example is below:

    [ [], [], [], [], [], [], [] ] <--- This grid is empty
    [ [Card, Card], [], [], [Card], [], [], [] ] <--- This grid is NOT empty

params:
    grid - a 2D list in the format shown above

returns:
    True if the grid is empty
    False if the grid is not empty

'''


def checkWin(grid):
    # iterating through each column
    for col in grid:
        # checking if the column is empty or not
        if col:
            return False
    return True

'''
Calculates the abs between the values of two cards
params:
    card1 - instance of the Card class
    card2 - instance of the Card class

returns:
    the absolute value between the two cards (accounting for A/J/Q/K)

'''


def compareCards(card1, card2):
    difference = abs(int(card1.value) - int(card2.value))
    # functionality for comparing ace and king
    if difference == 12:
        return 1
    else:
        return difference





def main():
    deck = Deck() # initialize deck
    game_is_on = True # creating a value to create a loop for the game to run
    grid = initGrid(deck)
    waste_card = deck.drawCard()
    while game_is_on:
        displayGrid(grid)
        print(f"Waste card: {waste_card}")
        choice = input("Enter an index to remove or 'd' to draw or 'q' to quit: ")
        if choice == "d":
            if deck.cardsLeft() == 0:
                print("Deck is empty")
            else:
                waste_card = deck.drawCard()
        elif choice == "q":
            game_is_on = False
        else:
            index = int(choice)
            if index > 6 or index < 0:
                print("Choose valid index")
            else:
                card = grid[index][0]
                if compareCards(card,waste_card) != 1:
                    print("Selected card cannot be moved")
                else:
                    waste_card = card
                    grid[index].pop(0)

        if checkWin(grid):
            print("You Won!")
            game_is_on = False


if __name__ == "__main__":
    main()