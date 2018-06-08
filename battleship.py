##Battleship

import random as r
import answer as a

def main():
    print("BBBBB   AAAA  TTTTTT TTTTTT LL     EEEEEE  SSSS  HH  HH IIIIII PPPPP \nBB  BB AA  AA   TT     TT   LL     EE     SS  SS HH  HH   II   PP  PP\nBBBBB  AA  AA   TT     TT   LL     EEEE    SS    HHHHHH   II   PP  PP\nBB  BB AAAAAA   TT     TT   LL     EE        SS  HH  HH   II   PPPPP \nBB  BB AA  AA   TT     TT   LL     EE     SS  SS HH  HH   II   PP    \nBBBBB  AA  AA   TT     TT   LLLLLL EEEEEE  SSSS  HH  HH IIIIII PP ")
    if input("\nPlay a game? ")[0].lower() == 'y':
        play()
    else:
        raise SystemExit

def play():
    size, attempts = 5, 10
    answer = r.choice(a.answerGen(size))
    guess(size, attempts, answer)

def guess(size, attempts, answer):
    blank = [[], ['   A', 'B', 'C', 'D', 'E'], [], ['1 ','.', '.' ,'.', '.', '.'], ['2 ', '.', '.' ,'.', '.', '.'], ['3 ', '.', '.' ,'.', '.', '.'], ['4 ', '.', '.' ,'.', '.', '.'], ['5 ', '.', '.' ,'.', '.', '.'], []]
    while attempts != 0:
        display(blank)
        print("You have %s attempts left." % attempts)
        if attempts == 10:
            g = input("Enter your guess (eg. D2): ")
        else:
            g = input("Enter your guess: ")
        if g[0].upper() not in ['A', 'B', 'C', 'D', 'E'] or (g[1] not in ['1', '2', '3', '4', '5']):
            print("\nInvalid guess. Try again.\n")
            guess(size, attempts, answer)
        else:
            print("wip")#work in progess
        

def display(lst):
    for line in lst:
        for i in line:
            print(i, end=' ')
        print()

main()
