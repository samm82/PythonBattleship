import answerFull as aF
import random as r
import classicComp
import os, sys

class HiddenPrints:
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = None

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self._original_stdout

def main():
    atts = getAttempts()
    easy   = [test(classicComp, 0) for _ in range(atts)]
    medium = [test(classicComp, 1) for _ in range(atts)]
    hard   = [test(classicComp, 2) for _ in range(atts)]
    eAvg, mAvg, hAvg = sum(easy)/atts, sum(medium)/atts, sum(hard)/atts
    print("Easy:   {:5.2f}".format(eAvg))
    print("Medium: {:5.2f}".format(mAvg))
    print("Hard:   {:5.2f}".format(hAvg))
    print(len(easy), len(medium), len(hard))

def getAttempts():
    attempts = 0
    while attempts <= 0:
        test = input("Enter how many simulations to run: ")
        try:
            attempts = int(test)
            if attempts <= 0:
                print("You must enter an integer greater than zero.")
        except ValueError:
            print("You must enter an integer.")
    return attempts

def test(m, diff):
    c, bc, gL, t, h, tries = initialize(m, diff)
    #with HiddenPrints():
    while c != 17:  
        results = m.compGuess(c, bc, gL, t, h, diff)
        if results == None:
            continue
        else:
            c, bc, gL, t, h = results
        tries += 1
    return tries

def initialize(m, diff):
    c, bc, t, h, tries = 0, aF.fullGen(), [], [], 0
    for i in range(len(bc)):
        for j in range(len(bc[i])):
            if bc[i][j] == "O":
                bc[i][j] = "."
            elif bc[i][j] == "X":
                bc[i][j] = "#"
        bc[i] = ['']+bc[i]
    bc[-1].remove('')
    bc = [[],[],[],[],[]] + bc

    #GUESS LIST
    gL = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","J1","J2","J3","J4","J5","J6","J7","J8","J9","J10"]
    if diff == 2:
        left = ["A1","A3","A5","A7","A9","B2","B4","B6","B8","B10","C1","C3","C5","C7","C9","D2","D4","D6","D8","D10","E1","E3","E5","E7","E9","F2","F4","F6","F8","F10","G1","G3","G5","G7","G9","H2","H4","H6","H8","H10","I1","I3","I5","I7","I9","J2","J4","J6","J8","J10"]
        right = ["A2","A4","A6","A8","A10","B1","B3","B5","B7","B9","C2","C4","C6","C8","C10","D1","D3","D5","D7","D9","E2","E4","E6","E8","E10","F1","F3","F5","F7","F9","G2","G4","G6","G8","G10","H1","H3","H5","H7","H9","I2","I4","I6","I8","I10","J1","J3","J5","J7","J9"]
        gL = r.choice([left, right])

    return c, bc, gL, t, h, tries

main()