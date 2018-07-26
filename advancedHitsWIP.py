boatNames = ["patrol boat", "destroyer", "submarine", "battleship", "aircraft carrier"]
# therefore = boatLengths = [2, 3, 3, 4, 5] and can be referenced with the same indices
  # dictionaries?

hits = [[7, 2], [8, 2], [6, 2]] # [8, 2] is the patrol boat - hitting [9, 2] should remove both from the list

mostRecent = hits[-1]
hits.sort()

# x direction
stdX = mostRecent[0]
for i in hits[1:]:
    if i[0] = 

smallY = yHits[0] - 1
if smallY >= 0 and comp[smallY+5][stdX+1] not in ['O', 'X']:
    tempList.append([stdX, smallY])
bigY = yHits[-1] + 1
if bigY < 10 and comp[bigY+5][stdX+1] not in ['O', 'X']:
    tempList.append([stdX, bigY])

# y direction
stdY = mostRecent[0]
smallX = xHits[0] - 1
if smallX >= 0 and comp[stdY+5][smallX+1] not in ['O', 'X']:
    tempList.append([smallX, stdY])
bigX = xHits[-1] + 1
if bigX < 10 and comp[stdY+5][bigX+1] not in ['O', 'X']:
    tempList.append([bigX, stdY])