import string
import random

print("\nLet's play...")
print("                 _-_                   ")
print("               _| _ |_                 ")
print("       _______|_______|____            ")
print("      |_      |_______|  __| o   o   o ")
print("      |_SUPER BATTLESHIPS!_|           ")
print(" ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ")


cheatmode = (input("\nWould you like to use the cheat mode? (y or n): ")).lower()  # Allows you to view the whole board
if cheatmode == "y":
    print("Cheat mode turned on.")
elif cheatmode == "n":
    print("Cheat mode turned off.")

autoplace = (input("\nWould you like to place the ships automatically? (y or n): ")).lower()

#
#
# Set up master board:
#
#

board = []
board0 = ["0 "]

for n in range(0, 16):
    board0.append(string.ascii_lowercase[n] + "  ")  # Add extra spaces to keep the board layout consistent

board0.append("|")
board.append(board0)

for x in range(1, 10):  # One-digit numbers need an extra space, again to keep the board layout consistent
    x = (str(x) + " ")
    boardx = [x, "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ",
              "~~ ", "~~ ", "|"]
    board.append(boardx)

for x in range(10, 17):
    x = str(x)
    boardx = [x, "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ", "~~ ",
              "~~ ", "~~ ", "|"]
    board.append(boardx)

board.append("~~~" * 41)  # Bottom border


def cheatboard():  # Prints the entire board, including both player's ships
    print("\nCheat board:")
    for x in board:
        print(x)

ships1 = ["b1 ", "c1 ", "c2 ", "d1 ", "d2 ", "d3 ", "f1 ", "f2 ", "f3 ", "f4 "]  # List of Player 1's ships
ships2 = ["B1 ", "C1 ", "C2 ", "D1 ", "D2 ", "D3 ", "F1 ", "F2 ", "F3 ", "F4 "]  # List of Player 2's ships
hitships1 = ["b1H", "c1H", "c2H", "d1H", "d2H", "d3H", "f1H", "f2H", "f3H", "f4H"]  # Player 1's potential hit ships
hitships2 = ["B1h", "C1h", "C2h", "D1h", "D2h", "D3h", "F1h", "F2h", "F3h", "F4h"]  # Player 2's potential hit ships

vertical = []  # Create a list of horizontal and vertical ships so that we know in which directions they can move
horizontal = []
orientations = ["h", "v"]

#
#
# Place ships:
#
#


def placeship(player):
    global vertical
    global horizontal
    orient = "nil"
    if autoplace == "n":
        if player == 1:
            p1board()
            print("\nPLAYER 1: Place your ships on the left hand side (columns a-h)")
        else:
            p2board()
            print("\nPLAYER 2: Place your ships on the right hand side (columns i-p)")
    #
    #
    # BATTLESHIP
    #
    #
    verifymove = False  # We will use this to validate each ship placement
    #
    # Automatic placement:
    #
    if autoplace == "y":
        if player == 1:
            print("\nProgram will now place Player 1's ships automatically.")
        else:
            print("Program will now place Player 2's ships automatically.")
        orient = random.choice(orientations)
        while not verifymove:
            if orient == "h":
                if player == 1:
                    x = random.choice(range(1, 6))
                elif player == 2:
                    x = random.choice(range(9, 14))
                y = random.choice(range(1, 17))
                for n in range(0, 4):
                    if board[y][x + n] != "~~ ":  # Checks if there is another ship in the way
                        verifymove = False
                        break
                    else:
                        verifymove = True
            elif orient == "v":
                if player == 1:
                    x = random.choice(range(1, 9))
                elif player == 2:
                    x = random.choice(range(9, 17))
                y = random.choice(range(1, 14))
                for n in range(0, 4):
                    if board[y + n][x] != "~~ ":  # Checks if there is another ship in the way
                        verifymove = False
                        break
                    else:
                        verifymove = True
    #
    #  Manual placement:
    #
    elif autoplace == "n":
        print("\nPlace your Battleship (4 squares long):")
        orient = str(input("Would you like your ship to be vertical (v) or horizontal (h)?"))
        while not verifymove:
            if orient == "h":
                if player == 1:
                    letter = input("\nPick your x coordinate: ")
                    while (letter + "  ") not in board0:
                        letter = input("Try again: ")
                    x = board0.index(letter + "  ")
                    while x > 5:
                        x = board0.index(input("Stick to your own side! Pick your x coordinate: ") + "  ")
                elif player == 2:
                    letter = input("\nPick your x coordinate: ")
                    while (letter + "  ") not in board0:
                        letter = input("Try again: ")
                    x = board0.index(letter + "  ")
                    while (x <= 8) or (x > 13):
                        x = board0.index(input("Stick to your own side! Pick your x coordinate: ") + "  ")
                y = int(input("Pick your y coordinate: "))
                while y > 16:
                    y = int(input("Try again: "))
                for n in range(0, 4):
                    if board[y][x + n] != "~~ ":  # Checks if there is another ship in the way
                        verifymove = False
                        print("There is another ship in the way!")
                        break
                    else:
                        verifymove = True
            elif orient == "v":
                if player == 1:
                    letter = input("\nPick your x coordinate: ")
                    while (letter + "  ") not in board0:
                        letter = input("Try again: ")
                    x = board0.index(letter + "  ")
                    while x > 8:
                        x = board0.index(input("Stick to your own side! Pick your x coordinate: ") + "  ")
                elif player == 2:
                    letter = input("\nPick your x coordinate: ")
                    while (letter + "  ") not in board0:
                        letter = input("Try again: ")
                    x = board0.index(letter + "  ")
                    while x <= 8:
                        x = board0.index(input("Stick to your own side! Pick your x coordinate: ") + "  ")
                y = int(input("Pick your y coordinate: "))
                while y > 13:
                    y = int(input("Your ship will fall off the board! Try again: "))
                for n in range(0, 4):
                    if board[y + n][x] != "~~ ":  # Checks if there is another ship in the way
                        verifymove = False
                        print("There is another ship in the way!")
                        break
                    else:
                        verifymove = True
    #
    # Place ship:
    #
    if player == 1:
        if orient == "v":
            for n in range(0, 4):
                board[y + n][x] = "b1 "
            vertical.append("b1")
        elif orient == "h":
            for n in range(0, 4):
                board[y][x + n] = "b1 "
            horizontal.append("b1")
    elif player == 2:
        if orient == "v":
            for n in range(0, 4):
                board[y + n][x] = "B1 "
            vertical.append("B1")
        elif orient == "h":
            for n in range(0, 4):
                board[y][x + n] = "B1 "
            horizontal.append("B1")
    if autoplace == "n":
        if player == 1:
            p1board()
        else:
            p2board()
    #
    #
    # CRUISERS:
    #
    #
    if autoplace == "n":
        print("\nPlace two cruisers (3 squares long):")
    for ship in range(1, 3):
        verifymove = False
        #
        # Automatic placement:
        #
        if autoplace == "y":
            orient = random.choice(orientations)
            while not verifymove:
                if orient == "h":
                    if player == 1:
                        x = random.choice(range(1, 7))
                    elif player == 2:
                        x = random.choice(range(9, 15))
                    y = random.choice(range(1, 17))
                    for n in range(0, 3):
                        if board[y][x + n] != "~~ ":  # Checks if there is another ship in the way
                            verifymove = False
                            break
                        else:
                            verifymove = True
                elif orient == "v":
                    if player == 1:
                        x = random.choice(range(1, 9))
                    elif player == 2:
                        x = random.choice(range(9, 17))
                    y = random.choice(range(1, 15))
                    for n in range(0, 3):
                        if board[y + n][x] != "~~ ":  # Checks if there is another ship in the way
                            verifymove = False
                            break
                        else:
                            verifymove = True
        #
        # Manual placement:
        #
        elif autoplace == "n":
            print("\nCruiser", ship, ":")
            orient = str(input("Would you like your ship to be vertical (v) or horizontal (h)?"))
            while not verifymove:
                if orient == "h":
                    if player == 1:
                        letter = input("\nPick your x coordinate: ")
                        while (letter + "  ") not in board0:
                            letter = input("Try again: ")
                        x = board0.index(letter + "  ")
                        while x > 6:
                            x = board0.index(input("Stick to your own side! Pick another x coordinate: ") + "  ")
                    elif player == 2:
                        letter = input("\nPick your x coordinate: ")
                        while (letter + "  ") not in board0:
                            letter = input("Try again: ")
                        x = board0.index(letter + "  ")
                        while (x <= 8) or (x > 14):
                            x = board0.index(input("Stick to your own side! Pick another x coordinate: ") + "  ")
                    y = int(input("Pick your y coordinate: "))
                    while y > 16:
                        y = int(input("Try again: "))
                    for n in range(0, 3):
                        if board[y][x + n] != "~~ ":  # Checks if there is another ship in the way
                            verifymove = False
                            print("There is another ship in the way!")
                            break
                        else:
                            verifymove = True
                elif orient == "v":
                    if player == 1:
                        letter = input("\nPick your x coordinate: ")
                        while (letter + "  ") not in board0:
                            letter = input("Try again: ")
                        x = board0.index(letter + "  ")
                        while x > 8:
                            x = board0.index(input("Stick to your own side! Pick another x coordinate: ") + "  ")
                    elif player == 2:
                        letter = input("\nPick your x coordinate: ")
                        while (letter + "  ") not in board0:
                            letter = input("Try again: ")
                        x = board0.index(letter + "  ")
                        while x <= 8:
                            x = board0.index(input("Stick to your own side! Pick another x coordinate: ") + "  ")
                    y = int(input("Pick your y coordinate: "))
                    while y > 14:
                        y = int(input("Your ship will fall off the board! Pick another y coordinate: "))
                    for n in range(0, 3):
                        if board[y + n][x] != "~~ ":  # Checks if there is another ship in the way
                            verifymove = False
                            print("There is another ship in the way!")
                            break
                        else:
                            verifymove = True
        #
        #  Place ship:
        #
        if player == 1:
            if orient == "v":
                for n in range(0, 3):
                    board[y + n][x] = "c" + str(ship) + " "
                vertical.append("c" + str(ship))
            elif orient == "h":
                for n in range(0, 3):
                    board[y][x + n] = "c" + str(ship) + " "
                horizontal.append("c" + str(ship))
            if autoplace == "n":
                p1board()
        elif player == 2:
            if orient == "v":
                for n in range(0, 3):
                    board[y + n][x] = "C" + str(ship) + " "
                vertical.append("C" + str(ship))
            elif orient == "h":
                for n in range(0, 3):
                    board[y][x + n] = "C" + str(ship) + " "
                horizontal.append("C" + str(ship))
            if autoplace == "n":
                p2board()
    #
    #
    # DESTROYERS:
    #
    #
    if autoplace == "n":
        print("\nPlace three destroyers (2 squares long):")
    for ship in range(1, 4):
        verifymove = False
        #
        # Automatic placement:
        #
        if autoplace == "y":
            orient = random.choice(orientations)
            while not verifymove:
                if orient == "h":
                    if player == 1:
                        x = random.choice(range(1, 8))
                    elif player == 2:
                        x = random.choice(range(9, 16))
                    y = random.choice(range(1, 17))
                    for n in range(0, 2):
                        if board[y][x + n] != "~~ ":  # Checks if there is another ship in the way
                            verifymove = False
                            break
                        else:
                            verifymove = True
                elif orient == "v":
                    if player == 1:
                        x = random.choice(range(1, 9))
                    elif player == 2:
                        x = random.choice(range(9, 17))
                    y = random.choice(range(1, 16))
                    for n in range(0, 2):
                        if board[y + n][x] != "~~ ":  # Checks if there is another ship in the way
                            verifymove = False
                            break
                        else:
                            verifymove = True
        #
        # Manual placement:
        #
        elif autoplace == "n":
            print("\nDestroyer", ship, ":")
            orient = str(input("Would you like your ship to be vertical (v) or horizontal (h)?"))
            while not verifymove:
                if orient == "h":
                    if player == 1:
                        letter = input("\nPick your x coordinate: ")
                        while (letter + "  ") not in board0:
                            letter = input("Try again: ")
                        x = board0.index(letter + "  ")
                        while x > 7:
                            x = board0.index(input("Stick to your own side! Pick another x coordinate: ") + "  ")
                    elif player == 2:
                        letter = input("\nPick your x coordinate: ")
                        while (letter + "  ") not in board0:
                            letter = input("Try again: ")
                        x = board0.index(letter + "  ")
                        while (x <= 8) or (x > 15):
                            x = board0.index(input("Stick to your own side! Pick another x coordinate: ") + "  ")
                    y = int(input("Pick your y coordinate: "))
                    while y > 16:
                        y = int(input("Try again: "))
                    for n in range(0, 2):
                        if board[y][x + n] != "~~ ":  # Checks if there is another ship in the way
                            verifymove = False
                            print("There is another ship in the way!")
                            break
                        else:
                            verifymove = True
                elif orient == "v":
                    if player == 1:
                        letter = input("\nPick your x coordinate: ")
                        while (letter + "  ") not in board0:
                            letter = input("Try again: ")
                        x = board0.index(letter + "  ")
                        while x > 8:
                            x = board0.index(input("Stick to your own side! Pick another x coordinate: ") + "  ")
                    elif player == 2:
                        letter = input("\nPick your x coordinate: ")
                        while (letter + "  ") not in board0:
                            letter = input("Try again: ")
                        x = board0.index(letter + "  ")
                        while x <= 8:
                            x = board0.index(input("Stick to your own side! Pick another x coordinate: ") + "  ")
                    y = int(input("Pick your y coordinate: "))
                    while y > 15:
                        y = int(input("Your ship will fall off the board! Pick another y coordinate: "))
                    for n in range(0, 2):
                        if board[y + n][x] != "~~ ":  # Checks if there is another ship in the way
                            verifymove = False
                            print("There is another ship in the way!")
                            break
                        else:
                            verifymove = True
        #
        # Place ship:
        #
        if player == 1:
            if orient == "v":
                for n in range(0, 2):
                    board[y + n][x] = "d" + str(ship) + " "
                vertical.append("d" + str(ship))
            elif orient == "h":
                for n in range(0, 2):
                    board[y][x + n] = "d" + str(ship) + " "
                horizontal.append("d" + str(ship))
            if autoplace == "n":
                p1board()
        else:
            if orient == "v":
                for n in range(0, 2):
                    board[y + n][x] = "D" + str(ship) + " "
                vertical.append("D" + str(ship))
            elif orient == "h":
                for n in range(0, 2):
                    board[y][x + n] = "D" + str(ship) + " "
                horizontal.append("D" + str(ship))
            if autoplace == "n":
                p2board()
    #
    #
    # FRIGATES:
    #
    #
    if autoplace == "n":
        print("\nPlace four frigates (1 square long):")
    for ship in range(1, 5):
        verifymove = False
        #
        # Automatic placement:
        #
        if autoplace == "y":
            while not verifymove:
                if player == 1:
                    x = random.choice(range(1, 9))
                elif player == 2:
                    x = random.choice(range(9, 17))
                y = random.choice(range(1, 17))
                if board[y][x] != "~~ ":
                    verifymove = False
                else:
                    verifymove = True
        #
        # Manual placement:
        #
        elif autoplace == "n":
            print("\nFrigate", ship, ":")
            while not verifymove:
                if player == 1:
                    letter = input("\nPick your x coordinate: ")
                    while (letter + "  ") not in board0:
                        letter = input("Try again: ")
                    x = board0.index(letter + "  ")
                    while x > 8:
                        x = board0.index(input("Stick to your own side! Pick your x coordinate: ") + "  ")
                elif player == 2:
                    letter = input("\nPick your x coordinate: ")
                    while (letter + "  ") not in board0:
                        letter = input("Try again: ")
                    x = board0.index(letter + "  ")
                    while x <= 8:
                        x = board0.index(input("Stick to your own side! Pick your x coordinate: ") + "  ")
                y = int(input("Pick your y coordinate: "))
                while y > 16:
                    y = int(input("Try again: "))
                if board[y][x] != "~~ ":
                    verifymove = False
                    print("There is another ship in the way!")
                else:
                    verifymove = True
        #
        # Place ship:
        #
        if player == 1:
            board[y][x] = "f" + str(ship) + " "
            if autoplace == "n":
                p1board()
        elif player == 2:
            board[y][x] = "F" + str(ship) + " "
            if autoplace == "n":
                p2board()
    if cheatmode == "y":
        cheatboard()
    else:
        if player == 1:
            p1board()
        else:
            p2board()
    input("\nPress enter when the next player is ready.")
    print("\n" * 40)  # Print blank lines to clear the screen between players

#
#
# Print a separate board for each player:
#
#

allships1 = []  # Create a list of all of Player 1's ships, hit and not hit
for x in ships1:
    allships1.append(x)
for x in hitships1:
    allships1.append(x)

allships2 = []  # Create a list of all of Player 2's ships, hit and not hit
for x in ships2:
    allships2.append(x)
for x in hitships2:
    allships2.append(x)


def p1board():
    print("\nPlayer 1's board:")
    player1board = []
    for num in board:
        num2 = num[:]
        player1board.append(num2)  # Copies the board to create Player 1's view
    for num in player1board:
        for i in range(len(num)):
            if num[i] in ships2:
                y = player1board.index(num)  # Check if any of Player 2's ships are touching Player 1's ships
                x = i
                if player1board[y - 1][x - 1] not in allships1 and \
                    player1board[y][x - 1] not in allships1 and \
                    player1board[y + 1][x - 1] not in allships1 and \
                    player1board[y - 1][x] not in allships1 and \
                    player1board[y + 1][x] not in allships1 and \
                    player1board[y - 1][x + 1] not in allships1 and \
                    player1board[y][x + 1] not in allships1 and \
                    player1board[y + 1][x + 1] not in allships1:
                        player1board[y][x] = "~~ "  # If not, these ships cannot be seen by Player 1
        print(num)


def p2board():
    print("\nPlayer 2's board:")
    player2board = []
    for num in board:
        num2 = num[:]
        player2board.append(num2)  # Copies the board to create Player 2's view
    for num in player2board:
        for i in range(len(num)):
            if num[i] in ships1:
                y = player2board.index(num)  # Check if any of Player 1's ships are touching Player 2's ships
                x = i
                if player2board[y - 1][x - 1] not in allships2 and \
                    player2board[y][x - 1] not in allships2 and \
                    player2board[y + 1][x - 1] not in allships2 and \
                    player2board[y - 1][x] not in allships2 and \
                    player2board[y + 1][x] not in allships2 and \
                    player2board[y - 1][x + 1] not in allships2 and \
                    player2board[y][x + 1] not in allships2 and \
                    player2board[y + 1][x + 1] not in allships2:
                        player2board[y][x] = "~~ "  # If not, these ships cannot be seen by Player 2
        print(num)


placeship(1)
placeship(2)
print("\nBegin play!")

#
#
# Directional functions:
#
#


def left(player, piece):  # Moving left: decrease the x index by one
    verifymove = "nil"  # These variables must be re-set each time
    xindex = []
    yindex = []
    hitornot = []
    for num in board:
        if num == board[0]:
            num = board[1]
        for l in range(len(num)):
            if piece in num[l]:
                xindex.append(l)
                yindex.append(board.index(num))
    for y, x in zip(yindex, xindex):
        if ("h" in board[y][x]) or ("H" in board[y][x]):  # Check if any part of the ship has been hit and store this
            hitornot.append("h")
        else:
            hitornot.append(" ")
        if (board[y][x - 1] == "~~ ") or (piece in board[y][x - 1]) or (board[y][x - 1] in ["m  ", "M  "]):
            verifymove = True
        else:
            verifymove = False
            break
    if not verifymove:
        print("\nYou cannot move there.")
    elif verifymove:
        for r, c, h in zip(yindex, xindex, hitornot):
            board[r][c] = "~~ "
            if player == 1:
                board[r][c - 1] = piece + str(h).upper()
            elif player == 2:
                board[r][c - 1] = piece + h


def right(player, piece):  # Moving right: increase the x index by one
    verifymove = "nil"  # These variables must be re-set each time
    xindex = []
    yindex = []
    hitornot = []
    for num in board:
        if num == board[0]:
            num = board[1]
        for l in range(len(num)):
            if piece in num[l]:
                xindex.append(l)
                yindex.append(board.index(num))
    for y, x in zip(yindex, xindex):
        if ("h" in board[y][x]) or ("H" in board[y][x]):  # Check if any part of the ship has been hit and store this
            hitornot.append("h")
        else:
            hitornot.append(" ")
        if (board[y][x + 1] == "~~ ") or (piece in board[y][x + 1]) or (board[y][x + 1] in ["m  ", "M  "]):
            verifymove = True
        else:
            verifymove = False
            break
    if not verifymove:
        print("\nYou cannot move there.")
    elif verifymove:
        for r, c, h in zip(yindex[::-1], xindex[::-1], hitornot[::-1]):  # Traverse the lists backwards to move right
            board[r][c] = "~~ "
            if player == 1:
                board[r][c + 1] = piece + str(h).upper()
            elif player == 2:
                board[r][c + 1] = piece + h


def up(player, piece):  # Moving up: decrease the y index by one
    verifymove = "nil"  # These variables must be re-set each time
    xindex = []
    yindex = []
    hitornot = []
    for num in board:
        if num == board[0]:
            num = board[1]
        for l in range(len(num)):
            if piece in num[l]:
                xindex.append(l)
                yindex.append(board.index(num))
    for y, x in zip(yindex, xindex):
        if ("h" in board[y][x]) or ("H" in board[y][x]):  # Check if any part of the ship has been hit and store this
            hitornot.append("h")
        else:
            hitornot.append(" ")
        if (board[y - 1][x] == "~~ ") or (piece in board[y - 1][x]) or (board[y - 1][x] in ["m  ", "M  "]):
            verifymove = True
        else:
            verifymove = False
            break
    if not verifymove:
        print("\nYou cannot move there.")
    elif verifymove:
        for r, c, h in zip(yindex, xindex, hitornot):
            board[r][c] = "~~ "
            if player == 1:
                board[r - 1][c] = piece + str(h).upper()
            elif player == 2:
                board[r - 1][c] = piece + h


def down(player, piece):  # Moving down: increase the y index by one
    verifymove = "nil"  # These variables must be re-set each time
    xindex = []
    yindex = []
    hitornot = []
    for num in board:
        if num == board[0]:
            num = board[1]
        for l in range(len(num)):
            if piece in num[l]:
                xindex.append(l)
                yindex.append(board.index(num))
    for y, x in zip(yindex, xindex):
        if ("h" in board[y][x]) or ("H" in board[y][x]):  # Check if any part of the ship has been hit and store this
            hitornot.append("h")
        else:
            hitornot.append(" ")
        if (board[y + 1][x] == "~~ ") or (piece in board[y + 1][x]) or (board[y + 1][x] in ["m  ", "M  "]):
            verifymove = True
        else:
            verifymove = False
            break
    if not verifymove:
        print("\nYou cannot move there.")
    elif verifymove:
        for r, c, h in zip(yindex[::-1], xindex[::-1], hitornot[::-1]):  # Traverse the lists backwards to move down
            board[r][c] = "~~ "
            if player == 1:
                board[r + 1][c] = piece + str(h).upper()
            elif player == 2:
                board[r + 1][c] = piece + h

#
#
# Begin play!
#
#


def player1():
    if cheatmode == "y":
        cheatboard()
    else:
        p1board()
    print("\nPLAYER 1:")
    play = input("\nWould you like to shoot or move? ")
    if play == "shoot":
        letter = input("\nPick your x coordinate: ")
        while (letter + "  ") not in board0:
            letter = input("Not valid! Pick another x coordinate: ")
        x = board0.index(letter + "  ")
        y = int(input("Pick your y coordinate: "))
        while y > 16:
            y = int(input("Not valid! Pick another y coordinate: "))
        if "h" in board[y][x]:
            print("You have already hit this part of the ship!")
        elif board[y][x] in ships2:
            print("\nHit!")
            board[y][x] = board[y][x].replace(" ", "")
            board[y][x] = (board[y][x] + "h")
        elif board[y][x] == "~~ ":
            print("\nMiss!")
            board[y][x] = "m  "
    elif play == "move":
        piece = str(input("\nWrite the full name of the piece you would like to move: "))
        while (piece + " ") not in ships1:
            piece = str(input("That is not your ship! Try again: "))
        while piece in sunk1:
            piece = str(input("That ship has sunk! Try again: "))
        while (piece + "H") in sunk1:
            piece = str(input("That ship has sunk! Try again: "))
        if piece in vertical:
            direction = str(input("Would you like to move up (u) or down (d)? "))
            if (direction == "l") or (direction == "r"):
                direction = str(input("You cannot move in that direction! Try again: "))
        elif piece in horizontal:
            direction = str(input("Would you like to move left (l) or right (r)?"))
            if (direction == "u") or (direction == "d"):
                direction = str(input("You cannot move in that direction! Try again: "))
        else:
            direction = str(input("Would you like to move up (u), down (d), left (l) or right (r)? "))
        if direction == "l":
            left(1, piece)
        elif direction == "r":
            right(1, piece)
        elif direction == "u":
            up(1, piece)
        elif direction == "d":
            down(1, piece)
    if cheatmode == "y":
        cheatboard()
    else:
        p1board()
    input("\nPress enter when the next player is ready.")
    print("\n" * 40)


def player2():
    if cheatmode == "y":
        cheatboard()
    else:
        p2board()
    print("\nPLAYER 2:")
    play = input("\nWould you like to shoot or move? ")
    if play == "shoot":
        letter = input("\nPick your x coordinate: ")
        while (letter + "  ") not in board0:
            letter = input("Not valid! Pick another x coordinate: ")
        x = board0.index(letter + "  ")
        y = int(input("Pick your y coordinate: "))
        while y > 16:
            y = int(input("Not valid! Pick another y coordinate: "))
        if "H" in board[y][x]:
            print("You have already hit this part of the ship!")
        elif board[y][x] in ships1:
            print("\nHit!")
            board[y][x] = board[y][x].replace(" ", "")
            board[y][x] = (board[y][x] + "H")
        elif board[y][x] == "~~ ":
            print("\nMiss!")
            board[y][x] = "M  "
    elif play == "move":
        piece = str(input("\nWrite the full name of the piece you would like to move: "))
        while (piece + " ") not in ships2:
            piece = str(input("That is not your ship! Try again: "))
        while piece in sunk2:
            piece = str(input("That ship has sunk! Try again: "))
        while (piece + "h") in sunk2:
            piece = str(input("That ship has sunk! Try again: "))
        if piece in vertical:
            direction = str(input("Would you like to move up (u) or down (d)? "))
            if (direction == "l") or (direction == "r"):
                direction = str(input("You cannot move in that direction! Try again: "))
        elif piece in horizontal:
            direction = str(input("Would you like to move left (l) or right (r)?"))
            if (direction == "u") or (direction == "d"):
                direction = str(input("You cannot move in that direction! Try again: "))
        else:
            direction = str(input("Would you like to move up (u), down (d), left (l) or right (r)? "))
        if direction == "l":
            left(2, piece)
        elif direction == "r":
            right(2, piece)
        elif direction == "u":
            up(2, piece)
        elif direction == "d":
            down(2, piece)
    if cheatmode == "y":
        cheatboard()
    else:
        p2board()
    input("\nPress enter when the next player is ready.")
    print("\n" * 40)

#
#
# Check which ships have been sunk:
#
#

sunk1 = []  # Create lists of each player's sunken ships
sunk2 = []


def checksunk1():  # Check which of Player 1's ships have been sunk
    global sunk1
    for s in hitships1:
        times = 0
        for num in board:
            for l in range(len(num)):
                if num[l] == s:
                    times += 1  # Count how many parts of each ship have been hit; if all parts, the ship is sunk
        if "b" in s:
            if times == 4:  # A Battleship is 4 squares long
                if s not in sunk1:
                    sunk1.append(s)  # If it is not already in the list of sunk ships, add it
        elif "c" in s:
            if times == 3:  # A Cruiser is 3 squares long, etc.
                if s not in sunk1:
                    sunk1.append(s)
        elif "d" in s:
            if times == 2:
                if s not in sunk1:
                    sunk1.append(s)
        elif "f" in s:
            if times == 1:
                if s not in sunk1:
                    sunk1.append(s)
    print("Player 1's", sunk1, "has been sunk.")


def checksunk2():  # Check which of Player 2's ships have been sunk
    global sunk2
    for s in hitships2:
        times = 0
        for num in board:
            for l in range(len(num)):
                if num[l] == s:
                    times += 1
        if "B" in s:
            if times == 4:
                if s not in sunk2:
                    sunk2.append(s)
        elif "C" in s:
            if times == 3:
                if s not in sunk2:
                    sunk2.append(s)
        elif "D" in s:
            if times == 2:
                if s not in sunk2:
                    sunk2.append(s)
        elif "F" in s:
            if times == 1:
                if s not in sunk2:
                    sunk2.append(s)
    print("Player 2's", sunk2, "has been sunk.")


def gamewon():  # If all of a player's ships have been sunk, the game is over
    if {"B1h", "C1h", "C2h", "D1h", "D2h", "D3h", "F1h", "F2h", "F3h", "F4h"}.issubset(set(sunk2)):
        print("\nGAME OVER")
        print("\nCongratulations! Player 1 wins!")
        return True
    elif {"b1H", "c1H", "c2H", "d1H", "d2H", "d3H", "f1H", "f2H", "f3H", "f4H"}.issubset(set(sunk1)):
        print("\nGAME OVER")
        print("\nCongratulations! Player 2 wins!")
        return True


def playgame():
    while not gamewon():
        player1()
        checksunk2()
        if not gamewon():
            player2()
            checksunk1()

playgame()
