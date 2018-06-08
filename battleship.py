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
    size = 5
    answer = r.choice(a.answerGen(size))

def display(lst):
    for line in lst:
        for i in line:
            print(i, end=' ')
        print()

main()
