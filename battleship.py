##Battleship

import random as r

def main():
    print("BBBBB   AAAA  TTTTTT TTTTTT LL     EEEEEE  SSSS  HH  HH IIIIII PPPPP \nBB  BB AA  AA   TT     TT   LL     EE     SS  SS HH  HH   II   PP  PP\nBBBBB  AA  AA   TT     TT   LL     EEEE    SS    HHHHHH   II   PP  PP\nBB  BB AAAAAA   TT     TT   LL     EE        SS  HH  HH   II   PPPPP \nBB  BB AA  AA   TT     TT   LL     EE     SS  SS HH  HH   II   PP    \nBBBBB  AA  AA   TT     TT   LLLLLL EEEEEE  SSSS  HH  HH IIIIII PP ")
    if input("\nPlay a game? ")[0].lower() == 'y':
        play()
    else:
        raise SystemExit

def play():
    size = 5
    makeGrid(size)
    
def makeGrid(s):
    boatPos = []
    x, y = r.randint(0,5), r.randint(0,5)
    boatPos.append((x, y))
    orient, start = boatRandom()
    print(orient, start)
    grid = []

def boatRandom():
    orient, start = r.choice(['v', 'h', 'dl', 'dr']), r.randint(1,3)
    return orient, start
    

main()
