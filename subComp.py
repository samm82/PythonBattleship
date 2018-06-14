import answerSub as aS
import random as r
import display as d

def play(diff):
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
    guessList = ['A1', 'A2', 'A3', 'A4', 'A5', 'B1', 'B2', 'B3', 'B4', 'B5', 'C1', 'C2', 'C3', 'C4', 'C5', 'D1', 'D2', 'D3', 'D4', 'D5', 'E1', 'E2', 'E3', 'E4', 'E5']
    if diff == 2:
        guessList = halfGL(guessList)
    return pickShip(blankPlayer, blankComp, guessList)

def pickShip(blankP, blankC, gL):
    d.display(blankP)
    start = input("Enter the position of one end of your submarine: ")
    if (len(start)<2) or start[0].upper() not in ['A', 'B', 'C', 'D', 'E'] or (start[1] not in ['1', '2', '3', '4', '5']):
        print("\nINVALID INPUT. Try again.\n")
        pickShip(blankP, blankC, gL)
    else:
        x1, y1 = guessIdentify(start)
        end = input("Enter the position of the other end of your submarine: ")
        if (len(end)<2) or end[0].upper() not in ['A', 'B', 'C', 'D', 'E'] or (end[1] not in ['1', '2', '3', '4', '5']):
            print("\nINVALID INPUT. Try again.\n")
            pickShip(blankP, blankC, gL)
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
                pickShip(blankP, blankC, gL)
    size, pHits, cHits, t, h = 5, 0, 0, [], []
    answer = r.choice(aS.subGen())
    return size, pHits, cHits, answer, blankP, blankC, gL, t, h

def guess(p, answer, player, comp):
    d.displayBoth(player, comp)
    g = input("Enter your guess (eg. D2): ") #variable 'g' to not confuse with guess()
    if (len(g)<2) or g[0].upper() not in ['A', 'B', 'C', 'D', 'E'] or (g[1] not in ['1', '2', '3', '4', '5']):
        print("\nINVALID GUESS. Try again.\n")
        guess(p, answer, player, comp)
    else:
        x, y = guessIdentify(g)
        if player[y+5][x+1] != '.': # to navigate "filler" text for display to work properly
            print("\nYou already guessed here. Try again.\n")
            guess(p, answer, player, comp)
        else:
            player[y+5][x+1] = answer[x][y]
            if answer[x][y] == "O":
                print("\nMM    MM IIIIII  SSSS   SSSS \nMMM  MMM   II   SS  SS SS  SS\nMMMMMMMM   II    SS     SS   \nMM MM MM   II      SS     SS \nMM    MM   II   SS  SS SS  SS\nMM    MM IIIIII  SSSS   SSSS \n")
            elif answer[x][y] == "X":
                print("\nHH  HH IIIIII TTTTTT !!\nHH  HH   II     TT   !!\nHHHHHH   II     TT   !!\nHH  HH   II     TT   !!\nHH  HH   II     TT     \nHH  HH IIIIII   TT   !!\n")
                p += 1
            else:
                print("ERROR") #should never run, but just in case
    return p, answer, player, comp

def compGuess(c, comp, gL, tryHere, hits, d):
    if len(hits) >= 2 and (d == 2):
        tryHere = genTryFromHits(comp, tryHere, hits)
    if d >= 1 and tryHere:
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
        print("\nThe computer hit your submarine!\n")
        comp[y+5][x+1] = "X"
        if d >= 1:
            tryHere += genTryHere(comp, x, y)
        if d == 2:
            hits.append([x,y])
    else:
        print("ERROR") #should never run, but just in case
    return c, comp, gL, tryHere, hits

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
        if bigY < 5 and comp[bigY+5][stdX+1] not in ['O', 'X']:
            tempList.append([stdX, bigY])
    elif yHits[0] == yHits[-1]:
        stdY = YHits[0]
        smallX = xHits[0] - 1
        if smallX >= 0 and comp[stdY+5][smallX+1] not in ['O', 'X']:
            tempList.append([smallX, stdY])
        bigX = yHits[-1] + 1
        if bigX < 5 and comp[stdY+5][bigX+1] not in ['O', 'X']:
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
        
