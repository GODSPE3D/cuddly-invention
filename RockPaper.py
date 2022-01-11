# DISCLAIMER: Make sure to have all the libs for this program to work
# WRITTEN BY: Sharad Maurya (sharadmaurya29@gmail.com)

import random

# Declaring variables
a = 'Y'
computer = ['Rock', 'Paper', 'Scissors']


# If player WINS
def win():
    print("Congratulations!! YOU WON")


# If player LOSES
def lose():
    print("Oh No! YOU LOST")


# If the game TIES
def tie():
    print("Sorry! It's a TIE")


# Show Computer's Choice
def compch(x):
    print("Computer's choice was", ''.join(computer[x]))


# MAIN
while a == 'Y' or a == 'y':
    # MENU
    print("\n-----------------------------------------------\n Welcome to the OG game Rock, Paper, Scissors!"
          "\n-----------------------------------------------\n\nChoose an option from the menu to PLAY!"
          "\n ______________\n| 1. Paper     |\n| 2. Rock      |\n| 3. Scissors  |\n|______________|")
    # INPUT
    n = int(input("Enter digit: "))

    # 1st Option (PAPER)
    if n == 1:
        print('\nYou chose Paper')
        if random.choice(computer) == 'Rock':
            compch(0)
            win()
        elif random.choice(computer) == 'Scissors':
            compch(2)
            lose()
        else:
            tie()

    # 2nd Option (ROCK)
    elif n == 2:
        print('\nYou chose Rock')
        if random.choice(computer) == 'Scissors':
            compch(2)
            win()
        elif random.choice(computer) == 'Paper':
            compch(1)
            lose()
        else:
            tie()

    # 3rd Option (SCISSORS)
    elif n == 3:
        print('\nYou chose Scissors')
        if random.choice(computer) == 'Paper':
            compch(1)
            win()
        elif random.choice(computer) == 'Rock':
            compch(0)
            lose()
        else:
            tie()

    else:
        print("Invalid Input")

    a = str(input('\nPLAY/TRY again (Y/N)? : '))

else:
    print("\n-------- Thanks for PLaying! --------")
