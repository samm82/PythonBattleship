from display import display
import answerFull as aF
import random as r

def play():
    attempts, hits = 40, 0
    answer = aF.fullGen()
    blank = [[],
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
             ['10', '.', '.' ,'.', '.', '.', '.', '.' ,'.', '.', '.'],
             []]
    guess(attempts, hits, answer, blank)

def guess(attempts, hits, answer, blank):
    while attempts != 0:
        display(blank)
        print("You have %s attempts left." % attempts)
        if attempts == 40:
            g = input("Enter your guess (eg. D2): ") #variable 'g' to not confuse with guess()
        else:
            g = input("Enter your guess: ")
        if g[0].upper() in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] and g[1:2] == '10':
            x, y = guessIdentify(g)
            print(blank)
        elif (len(g)<2) or (g[0].upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']) or (g[1] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']):
            print("\nINVALID GUESS. Try again.\n")
            guess(attempts, hits, answer, blank)
        else:
            x, y = guessIdentify(g)
        if blank[y+3][x+1] != '.': # to navigate "filler" text for display to work properly
            print("\nYou already guessed here. Try again.\n")
            guess(attempts, hits, answer, blank)
        else:
            blank[y+3][x+1] = answer[x][y]
            if answer[x][y] == "O":
                print("\nMM    MM IIIIII  SSSS   SSSS \nMMM  MMM   II   SS  SS SS  SS\nMMMMMMMM   II    SS     SS   \nMM MM MM   II      SS     SS \nMM    MM   II   SS  SS SS  SS\nMM    MM IIIIII  SSSS   SSSS \n")
            elif answer[x][y] == "X":
                print("\nHH  HH IIIIII TTTTTT !!\nHH  HH   II     TT   !!\nHHHHHH   II     TT   !!\nHH  HH   II     TT   !!\nHH  HH   II     TT     \nHH  HH IIIIII   TT   !!\n")
                hits += 1
            else:
                print("ERROR") #should never run, but just in case
            attempts -= 1
        if hits == 17:
            display(blank)
            print("\nYY  YY  OOOO  UU  UU     WW    WW IIIIII NN  NN !!\nYY  YY OO  OO UU  UU     WW    WW   II   NNN NN !!\n YYYY  OO  OO UU  UU     WW WW WW   II   NNNNNN !!\n  YY   OO  OO UU  UU     WWWWWWWW   II   NN NNN !!\n  YY   OO  OO UU  UU     WWW  WWW   II   NN  NN   \n  YY    OOOO   UUUU      WW    WW IIIIII NN  NN !!\n")
            again()
    display(blank)
    print("\nYY  YY  OOOO  UU  UU     LL      OOOO   SSSS  EEEEEE\nYY  YY OO  OO UU  UU     LL     OO  OO SS  SS EE    \n YYYY  OO  OO UU  UU     LL     OO  OO  SS    EEEE  \n  YY   OO  OO UU  UU     LL     OO  OO    SS  EE    \n  YY   OO  OO UU  UU     LL     OO  OO SS  SS EE    \n  YY    OOOO   UUUU      LLLLLL  OOOO   SSSS  EEEEEE\n")
    print("The boat was here:\n")
    for i in range(5):
        for j in range(5):
            if answer[i][j] == "X":
                blank[j+3][i+1] = answer[i][j]
            else:
                continue
    display(blank)
    again()

def guessIdentify(g):
    guessLocation = [0, 9] #default is A10
    if g[0].upper() == 'B':
        guessLocation[0] = 1
    elif g[0].upper() == 'C':
        guessLocation[0] = 2
    elif g[0].upper() == 'D':
        guessLocation[0] = 3
    elif g[0].upper() == 'E':
        guessLocation[0] = 4
    elif g[0].upper() == 'F':
        guessLocation[0] = 5
    elif g[0].upper() == 'G':
        guessLocation[0] = 6
    elif g[0].upper() == 'H':
        guessLocation[0] = 7
    elif g[0].upper() == 'I':
        guessLocation[0] = 8
    elif g[0].upper() == 'J':
        guessLocation[0] = 9
    #else: not needed - default is 0
    if len(g) != 3:
        guessLocation[1] = int(g[1]) - 1 #minus one to convert A1 to [0, 0] etc.
    print(guessLocation)
    return guessLocation[0], guessLocation[1]

play()
