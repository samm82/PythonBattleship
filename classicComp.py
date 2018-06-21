import display as d
import answerFull as aF
import random as r

def play(diff):
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
    guessList = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","J1","J2","J3","J4","J5","J6","J7","J8","J9","J10"]
    if diff == 2:
        guessList = halfGL(guessList)
    d.displayBoth(blankPlayer, blankComp)
    return pickShip(blankPlayer, blankPlayer, guessList)
    #size, attempts, hits, answer, blankPlayer, checkList

def pickShip(blankP, blankC, gL):
    # FOR TESTING - REVERT
    # ships = 0
    # shipList = ["patrol boat (2)", "destroyer (3)", "submarine (3)", "battleship (4)", "aircraft carrier (5)"]
    # while ships != 5:
    #     d.display(blankP)
    #     start = input("Enter the position of one end of your %s: " % shipList[ships])
    #     if (len(start)<2) or (start[0].upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) or (start[1:] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
    #         print("\nINVALID INPUT. Try again.\n")
    #     else:
    #         x1, y1 = guessIdentify(start)
    #         end = input("Enter the position of the other end of your %s: " % shipList[ships])
    #         if (len(end)<2) or (end[0].upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) or (end[1:] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
    #             print("\nINVALID INPUT. Try again.\n")
    #         else:
    #             x2, y2 = guessIdentify(end)
    #             print(abs(x1 - x2) + 1, abs(y1 - y2) + 1, int(shipList[ships][-2]))
    #             print(abs(x1 - x2) + 1 == int(shipList[ships][-2]))
    #             print(abs(y1 - y2) + 1 == int(shipList[ships][-2]))
    #             if abs(x1 - x2) + 1 == int(shipList[ships][-2]) and (y1 == y2):
    #                 small = min([x1, x2]) + 1
    #                 y = y1 + 5
    #                 for i in range(int(shipList[ships][-2])):
    #                     blankC[y][small+i] = "#"
    #                 ships += 1
    #             elif x1 == x2 and (abs(y1 - y2) + 1 == int(shipList[ships][-2])):
    #                 small = min([y1, y2]) + 5
    #                 x = x1 + 1
    #                 for i in range(int(shipList[ships][-2])):
    #                     blankC[small+i][x] = "#"
    #                 ships += 1
    #             else:
    #                 print("\nINVALID BOAT POSITION. Your {0} is {1} spaces long and cannot be diagonal - try again.\n".format(shipList[ships][:-4], shipList[ships][-2]))
    blankC = [[], ['           COMP      '], [],
                   ['   A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], [],
                   ['1 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['2 ', '.', '#' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['3 ', '.', '#' ,'.', '.', '#', '#', '#' ,'#', '.', '.'],
                   ['4 ', '.', '#' ,'.', '#', '.', '.', '.' ,'.', '.', '.'],
                   ['5 ', '.', '#' ,'.', '#', '.', '.', '.' ,'.', '.', '.'],
                   ['6 ', '.', '#' ,'.', '#', '.', '.', '.' ,'.', '.', '.'],
                   ['7 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['8 ', '.', '.' ,'.', '.', '.', '.', '#' ,'#', '.', '.'],
                   ['9 ', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
                   ['10', '#', '#' ,'#', '.', '.', '.', '.' ,'.', '.', '.'], []]
                   # ^^^REMOVE^^^
    size, pHits, cHits, t, h, ships = 5, 0, 0, [], [], 0
    answer = aF.fullGen()
    patrolBoatSunk, destroyerSunk, submarineSunk, battleshipSunk, aircraftCarrierSunk = False, False, False, False, False #initializes for checkBoats
    checkList = [patrolBoatSunk, destroyerSunk, submarineSunk, battleshipSunk, aircraftCarrierSunk, ships]
    d.displayBoth(blankP, blankC)
    d.display(answer)
    return size, pHits, cHits, answer, blankP, blankC, gL, t, h, checkList

def guess(p, answer, player, comp, cL):
    d.displayBoth(player, comp)
    g = input("Enter your guess (eg. D2) or 'menu' to return to menu: ") #variable 'g' to not confuse with guess()
    if (len(g)>1) and g.lower() in ['menu', 'quit', 'back', 'kill', 'no', 'nope', 'exit']:
        p = 'menu'
    elif (len(g)<2) or (g[0].upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) or (g[1:] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
        print("\nINVALID GUESS. Try again.\n")
        return None
    else:
        x, y = guessIdentify(g)
        if player[y+5][x+1] != '.': # to navigate "filler" text for display to work properly
            print("\nYou already guessed here. Try again.\n")
            return None
        else:
            print(x, y)
            print(x+1, y+5)
            print(player[y+5][x+1])
            d.display(answer)
            print(answer[x][y])
            player[y+5][x+1] = answer[x][y]
            if answer[x][y] == "O":
                print("\nMM    MM IIIIII  SSSS   SSSS \nMMM  MMM   II   SS  SS SS  SS\nMMMMMMMM   II    SS     SS   \nMM MM MM   II      SS     SS \nMM    MM   II   SS  SS SS  SS\nMM    MM IIIIII  SSSS   SSSS \n")
            elif answer[x][y] == "X":
                print("\nHH  HH IIIIII TTTTTT !!\nHH  HH   II     TT   !!\nHHHHHH   II     TT   !!\nHH  HH   II     TT   !!\nHH  HH   II     TT     \nHH  HH IIIIII   TT   !!\n")
                p += 1
                checkBoats(answer[-1], [x, y], cL)
            else:
                print("ERROR") #should never run, but just in case
    return [p, answer, player, comp, cL]


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

def halfGL(lst):
    left, right = [], []
    for i in range(len(lst)):
        if i % 2 == 0:
            left.append(lst[i])
        else:
            right.append(lst[i])
    return r.choice([left, right])