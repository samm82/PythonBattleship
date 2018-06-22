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
                   ['10', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'], [], [[], [], [], [], []]]
    guessList = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","J1","J2","J3","J4","J5","J6","J7","J8","J9","J10"]
    if diff == 2:
        guessList = halfGL(guessList)
    d.displayBoth(blankPlayer, blankComp[:-1])
    return pickShip(blankPlayer, blankComp, guessList)
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
    #         shipLength = int(shipList[ships][-2])
    #         else:
    #             x2, y2 = guessIdentify(end)
    #             print(abs(x1 - x2) + 1, abs(y1 - y2) + 1, shipLength)
    #             print(abs(x1 - x2) + 1 == shipLength)
    #             print(abs(y1 - y2) + 1 == shipLength)
    #             if abs(x1 - x2) + 1 == shipLength) and (y1 == y2):
    #                 small = min([x1, x2]) + 1
    #                 y = y1 + 5
    #                 for i in range(shipLength):
    #                     blankC[y][small+i] = "#"
    #                     blankC[-1][ships].append([small+i, y])  ###TO BE DOUBLE-CHECKED!!!
    #                 ships += 1
    #             elif x1 == x2 and (abs(y1 - y2) + 1 == shipLength):
    #                 small = min([y1, y2]) + 5
    #                 x = x1 + 1
    #                 for i in range(shipLength):
    #                     blankC[small+i][x] = "#"
    #                     blankC[-1][ships].append([x, small+i])  ###TO BE DOUBLE-CHECKED!!!
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
                   ['10', '#', '#' ,'#', '.', '.', '.', '.' ,'.', '.', '.'], [], 
                   [[[6, 7], [6, 8]], [[0, 9], [1, 9], [2, 9]], [[3, 3], [3, 4], [3, 5]], [[4, 2], [5, 2], [6, 2], [7, 2]], [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5]]]]
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
        return "menu"
    elif (len(g)<2) or (g[0].upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) or (g[1:] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']):
        print("\nINVALID GUESS. Try again.\n")
        return None
    else:
        x, y = guessIdentify(g)
        if player[y+5][x+1] != '.': # to navigate "filler" text for display to work properly
            print("\nYou already guessed here. Try again.\n")
            return None
        else:
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

def compGuess(c, comp, gL, tryHere, hits, diff):
    if len(hits) >= 2 and (diff == 2):
        tryHere = genTryFromHits(comp, tryHere, hits)
    if diff >= 1 and tryHere:
        gL = [x for x in gL if guessIdentify(x) not in tryHere]
        g = tryHere.pop(r.randrange(len(tryHere)))
        x, y = g[0], g[1]
    else:
        g = gL.pop(r.randrange(len(gL)))
        x, y = guessIdentify(g)
    if comp[y+5][x+1] == ".":
        print("\nThe computer missed.\n")
        comp[y+5][x+1] = "O"
    elif comp[y+5][x+1] == "#":
        c += 1
        boatList = comp[-1]
        if [x, y] in boatList[0]: #FIXME: pull out to function/module?
            boatList[0].remove([x, y])
            if boatList[0]:
                print("The computer hit your patrol boat!")
            else:
                print("The computer sunk your patrol boat!")
        elif [x, y] in boatList[1]:
            boatList[1].remove([x, y])
            if boatList[1]:
                print("The computer hit your destroyer!")
            else:
                print("The computer sunk your destroyer!")
        elif [x, y] in boatList[2]:
            boatList[2].remove([x, y])
            if boatList[2]:
                print("The computer hit your submarine!")
            else:
                print("The computer sunk your submarine!")
        elif [x, y] in boatList[3]:
            boatList[3].remove([x, y])
            if boatList[3]:
                print("The computer hit your battleship!")
            else:
                print("The computer sunk your battleship!")
        elif [x, y] in boatList[4]:
            boatList[4].remove([x, y])
            if boatList[4]:
                print("The computer hit your aircraft carrier!")
            else:
                print("The computer sunk your aircraft carrier!")
        else:
            print("ERROR") # probably should never run, but just in case
        comp[y+5][x+1] = "X"
        if diff >= 1:
            tryHere += genTryHere(comp, x, y)
        if diff == 2:
            hits.append([x,y])
    else:
        print("ERROR") #should never run, but just in case
    return c, comp, gL, tryHere, hits

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

def genTryHere(c, x, y):
    tryList = []
    if x+1 < 10:
        tryList.append([x+1, y])
    if x-1 >= 0:
        tryList.append([x-1, y])
    if y+1 < 10:
        tryList.append([x, y+1])
    if y-1 >= 0:
        tryList.append([x, y-1])
    for coord in tryList:
        if c[coord[1]+5][coord[0]+1] in ['O', 'X']:
            tryList.remove(coord) #optimize?
    return tryList

def genTryFromHits(comp, tryHere, hits):
    hits.sort()
    xHits, yHits = [], []
    for coord in hits:
        xHits.append(coord[0])
        yHits.append(coord[1])
    tempList = []
    if xHits[0] == xHits[-1]:
        stdX = xHits[0]
        smallY = yHits[0] - 1
        if smallY >= 0 and comp[smallY+5][stdX+1] not in ['O', 'X']:
            tempList.append([stdX, smallY])
        bigY = yHits[-1] + 1
        if bigY < 10 and comp[bigY+5][stdX+1] not in ['O', 'X']:
            tempList.append([stdX, bigY])
    elif yHits[0] == yHits[-1]:
        stdY = yHits[0]
        smallX = xHits[0] - 1
        if smallX >= 0 and comp[stdY+5][smallX+1] not in ['O', 'X']:
            tempList.append([smallX, stdY])
        bigX = yHits[-1] + 1
        if bigX < 10 and comp[stdY+5][bigX+1] not in ['O', 'X']:
            tempList.append([bigX, stdY])
    if tempList:
        tryHere = tempList
    return tryHere

def halfGL(lst):
    left, right = [], []
    for i in range(len(lst)):
        if i % 2 == 0:
            left.append(lst[i])
        else:
            right.append(lst[i])
    return r.choice([left, right])