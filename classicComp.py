from display import *
import answerFull as aF
import random as r

def play():
    size, attempts, hits, ships = 10, 40, 0, 5
    answer = aF.fullGen()
    blankPlayer = [[], ['         PLAYER      '], [],
                   ['   A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], [],
                   ['1 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['2 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['3 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['4 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['5 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['6 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['7 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['8 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['9 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['10', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'], []]
    blankComp   = [[], ['           COMP      '], [],
                   ['   A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], [],
                   ['1 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['2 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['3 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['4 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['5 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['6 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['7 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['8 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['9 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['10', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'], []]
    displayBoth(blankPlayer, blankComp)
    patrolBoatSunk, destroyerSunk, submarineSunk, battleshipSunk, aircraftCarrierSunk = False, False, False, False, False #initializes for checkBoats
    checkList = [patrolBoatSunk, destroyerSunk, submarineSunk, battleshipSunk, aircraftCarrierSunk, ships]
    return size, attempts, hits, answer, blankPlayer, checkList

def guess(attempts, hits, answer, blank, cL):
    display(blank)
    if attempts == 1 and (cL[-1] == 1):
        print("You have 1 attempt and 1 ship left.")
    elif attempts == 1:
        print("You have 1 attempt and {0} ships left.".format(cL[-1]))
    elif cL[-1] == 1:
        print("You have {0} attempts and 1 ship left.".format(attempts))
    else:
        print("You have {0} attempts and {1} ships left.".format(attempts, cL[-1]))
    if attempts == 40:
        g = input("Enter your guess (eg. D2): ") #variable 'g' to not confuse with guess()
    else:
        g = input("Enter your guess: ")
    g = "".join(g.split())
    if (len(g)>0) and g.lower() in ['menu', 'quit', 'back', 'kill', 'no', 'nope', 'exit']:
        return "menu"
    elif (len(g)<2) or (g[0].upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) or (g[1:] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
        print("\nINVALID GUESS. Try again.\n")
        return None
    else:
        x, y = guessIdentify(g)
        if blank[y+3][x+1] != '.': # to navigate "filler" text for display to work properly
            print("\nYou already guessed here. Try again.\n")
            return None
        else:
            blank[y+3][x+1] = answer[x][y]
            if answer[x][y] == "O":
                print("\nMM    MM IIIIII  SSSS   SSSS \nMMM  MMM   II   SS  SS SS  SS\nMMMMMMMM   II    SS     SS   \nMM MM MM   II      SS     SS \nMM    MM   II   SS  SS SS  SS\nMM    MM IIIIII  SSSS   SSSS \n")
            elif answer[x][y] == "X":
                print("\nHH  HH IIIIII TTTTTT !!\nHH  HH   II     TT   !!\nHHHHHH   II     TT   !!\nHH  HH   II     TT   !!\nHH  HH   II     TT     \nHH  HH IIIIII   TT   !!\n")
                hits += 1
                checkBoats(answer[-1], [x, y], cL)
            else:
                print("ERROR") #should never run, but just in case
            attempts -= 1
    return [attempts, hits, answer, blank, cL]


def checkBoats(boats, guess, cL):
    for i in boats:
        if guess in i:
            i.remove(guess)
    if not cL[0]:
        if boats[0] == []:
            print("Patrol boat sunk!")
            cL[-1] -= 1
            cL[0] = True
    if not cL[1]:
        if boats[1] == []:
            print("Destroyer sunk!")
            cL[-1] -= 1
            cL[1] = True
    if not cL[2]:
        if boats[2] == []:
            print("Submarine sunk!")
            cL[-1] -= 1
            cL[2] = True
    if not cL[3]:
        if boats[3] == []:
            print("Battleship sunk!")
            cL[-1] -= 1
            cL[3] = True
    if not cL[4]:
        if boats[4] == []:
            print("Aircraft carrier sunk!")
            cL[-1] -= 1
            cL[4] = True

def guessIdentify(g):
    x, y = 0, 9 #default is A10
    if g[0].upper() == 'B':
        x = 1
    elif g[0].upper() == 'C':
        x = 2
    elif g[0].upper() == 'D':
        x = 3
    elif g[0].upper() == 'E':
        x = 4
    elif g[0].upper() == 'F':
        x = 5
    elif g[0].upper() == 'G':
        x = 6
    elif g[0].upper() == 'H':
        x = 7
    elif g[0].upper() == 'I':
        x = 8
    elif g[0].upper() == 'J':
        x = 9
    #else: not needed - default is 0
    if len(g) != 3:
        y = int(g[1]) - 1 #minus one to convert A1 to [0, 0] etc.
    return x, y

play()