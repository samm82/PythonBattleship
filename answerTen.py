def answerGen(s):
    gridList = []
    for i in range(s):
        for j in range(s):
            gridList = horizontal(i, j, s, gridList)
            gridList = vertical(i, j, s, gridList)
    return gridList

def horizontal(x, y, s, gL):
    grid = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    if x+2 < s and x+1 < s: 
        grid[x][y], grid[x+1][y], grid[x+2][y] = 'X', 'X', 'X'
        gL.append(grid)
    return gL

def vertical(x, y, s, gL):
    grid = [['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O']]
    if y+2 < s and y+1 < s:
        grid[x][y], grid[x][y+1], grid[x][y+2] = 'X', 'X', 'X'
        gL.append(grid)
    return gL

answerGen(5)
