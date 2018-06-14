def subGen():
    gridList = []
    for i in range(5):
        for j in range(5):
            gridList = makeGrid(i, j, gridList)
    return gridList

def makeGrid(x, y, gL):
    gridH = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    if x+2 < 5 and x+1 < 5: 
        gridH[x][y], gridH[x+1][y], gridH[x+2][y] = 'X', 'X', 'X'
        gL.append(gridH)
    gridV = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    if y+2 < 5 and y+1 < 5:
        gridV[x][y], gridV[x][y+1], gridV[x][y+2] = 'X', 'X', 'X'
        gL.append(gridV)
    return gL