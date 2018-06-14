import answerSub as aS
import random as r
import display as d

def play():
    blankPlayer = [[], ['     PLAYER   '], [],
                   ['   A', 'B', 'C', 'D', 'E'], [],
                   ['1 ', '.', '.' ,'.', '.', '.'],
                   ['2 ', '.', '.' ,'.', '.', '.'],
                   ['3 ', '.', '.' ,'.', '.', '.'],
                   ['4 ', '.', '.' ,'.', '.', '.'],
                   ['5 ', '.', '.' ,'.', '.', '.'], []]
    blankComp = [[], ['   COMP   '], [],
                   ['   A', 'B', 'C', 'D', 'E'], [],
                   ['1 ', '.', '.' ,'.', '.', '.'],
                   ['2 ', '.', '.' ,'.', '.', '.'],
                   ['3 ', '.', '.' ,'.', '.', '.'],
                   ['4 ', '.', '.' ,'.', '.', '.'],
                   ['5 ', '.', '.' ,'.', '.', '.'], []]
    return pickShip(blankPlayer, blankComp)

def pickShip(blankP, blankC):
    d.display(blankP)
    start = input("Enter the position of one end of your submarine: ")
    if (len(start)<2) or start[0].upper() not in ['A', 'B', 'C', 'D', 'E'] or (start[1] not in ['1', '2', '3', '4', '5']):
        print("\nINVALID INPUT. Try again.\n")
        pickShip(blankP, blankC)
    else:
        x1, y1 = guessIdentify(start)
        end = input("Enter the position of the other end of your submarine: ")
        if (len(end)<2) or end[0].upper() not in ['A', 'B', 'C', 'D', 'E'] or (end[1] not in ['1', '2', '3', '4', '5']):
            print("\nINVALID INPUT. Try again.\n")
            pickShip(blankP, blankC)
        else:
            x2, y2 = guessIdentify(end)
            if abs(x1 - x2) == 2 and (y1 == y2):
                small = min([x1, x2]) + 1
                y = y1 + 5
                blankC[y][small], blankC[y][small+1], blankC[y][small+2] = '#', '#', '#'
            elif x1 == x2 and (abs(y1 - y2) == 2):
                small = min([y1, y2]) + 5
                x = x1 + 1
                blankC[small][x], blankC[small+1][x], blankC[small+2][x] = '#', '#', '#'
            else:
                print("\nINVALID BOAT POSITION. Your submarine is three spaces long and cannot be diagonal - try again.\n")
                pickShip(blankP, blankC)
    size, pHits, cHits, t, h = 5, 0, 0, [], []
    answer = r.choice(aS.subGen(5))
    return size, pHits, cHits, answer, blankP, blankC, t, h

def guess(p, c, answer, player, comp):
    d.displayBoth(player, comp)
    g = input("Enter your guess (eg. D2): ") #variable 'g' to not confuse with guess()
    if (len(g)<2) or g[0].upper() not in ['A', 'B', 'C', 'D', 'E'] or (g[1] not in ['1', '2', '3', '4', '5']):
        print("\nINVALID GUESS. Try again.\n")
        guess(p, c, answer, player, comp)
    else:
        x, y = guessIdentify(g)
        if player[y+5][x+1] != '.': # to navigate "filler" text for display to work properly
            print("\nYou already guessed here. Try again.\n")
            guess(p, c, answer, player, comp)
        else:
            player[y+5][x+1] = answer[x][y]
            if answer[x][y] == "O":
                print("\nMM    MM IIIIII  SSSS   SSSS \nMMM  MMM   II   SS  SS SS  SS\nMMMMMMMM   II    SS     SS   \nMM MM MM   II      SS     SS \nMM    MM   II   SS  SS SS  SS\nMM    MM IIIIII  SSSS   SSSS \n")
            elif answer[x][y] == "X":
                print("\nHH  HH IIIIII TTTTTT !!\nHH  HH   II     TT   !!\nHHHHHH   II     TT   !!\nHH  HH   II     TT   !!\nHH  HH   II     TT     \nHH  HH IIIIII   TT   !!\n")
                p += 1
            else:
                print("ERROR") #should never run, but just in case
    return p, c, answer, player, comp

def compGuess(p, c, answer, player, comp, tryHere, hits, d): #merge difficulties?
    if d == 0:
        g = r.choice(['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5'])
        x, y = guessIdentify(g)
        if comp[y+5][x+1] in ['O', 'X']: # to navigate "filler" text for display to work properly
            compGuess(p, c, answer, player, comp, tryHere, hits, d)
        else:
            if comp[y+5][x+1] == ".":
                print("\nThe computer missed.\n")
                comp[y+5][x+1] = "O"
            elif comp[y+5][x+1] == "#":
                print("\nThe computer hit your submarine!\n")
                comp[y+5][x+1] = "X"
                c += 1
            else:
                print("ERROR") #should never run, but just in case
    elif d == 1:
        if tryHere:
            g = tryHere.pop(r.randrange(len(tryHere)))
            x, y = g[0], g[1]
        else:
            g = r.choice(['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5'])
            x, y = guessIdentify(g)
        if comp[y+5][x+1] in ['O', 'X']: # +5 and +1 to navigate "filler" text for display to work properly
            # already guessed location, just tries again -> optimize?
            compGuess(p, c, answer, player, comp, tryHere, hits, d)
        else:
            if comp[y+5][x+1] == ".":
                print("\nThe computer missed.\n")
                comp[y+5][x+1] = "O"
            elif comp[y+5][x+1] == "#":
                print("\nThe computer hit your submarine!\n")
                comp[y+5][x+1] = "X"
                tryHere += genTryHere(comp, x, y)
                c += 1
            else:
                print("ERROR") #should never run, but just in case
    elif d == 2:
        if tryHere:
            g = tryHere.pop(r.randrange(len(tryHere)))
            x, y = g[0], g[1]
        else:
            g = r.choice(['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5'])
            x, y = guessIdentify(g)
        if comp[y+5][x+1] in ['O', 'X']: # +5 and +1 to navigate "filler" text for display to work properly
            # already guessed location, just tries again -> optimize?
            compGuess(p, c, answer, player, comp, tryHere, hits, d)
        else:
            if comp[y+5][x+1] == ".":
                print("\nThe computer missed.\n")
                comp[y+5][x+1] = "O"
            elif comp[y+5][x+1] == "#":
                print("\nThe computer hit your submarine!\n")
                comp[y+5][x+1] = "X"
                tryHere += genTryHere(comp, x, y)
                c += 1
            else:
                print("ERROR") #should never run, but just in case
    return p, c, answer, player, comp, tryHere, hits

def guessIdentify(g):
    guessLocation = [0, 0] #default is A1
    if g[0].upper() == 'B':
        guessLocation[0] = 1
    elif g[0].upper() == 'C':
        guessLocation[0] = 2
    elif g[0].upper() == 'D':
        guessLocation[0] = 3
    elif g[0].upper() == 'E':
        guessLocation[0] = 4
    #else: not needed - default is 0
    guessLocation[1] = int(g[1]) - 1 #minus one to convert A1 to [0, 0] etc.
    return guessLocation[0], guessLocation[1]

def genTryHere(c, x, y):
    tryList = []
    if x+1 < 5:
        tryList.append([x+1, y])
    if x-1 >= 0:
        tryList.append([x-1, y])
    if y+1 < 5:
        tryList.append([x, y+1])
    if y-1 >= 0:
        tryList.append([x, y-1])
    for coord in tryList:
        if c[coord[1]+5][coord[0]+1] in ['O', 'X']:
            tryList.remove(coord) #optimize?
    return tryList
