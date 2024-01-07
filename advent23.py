import sys

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"
matrix = [list(line.strip()) for line in open(f)]
longest = 0

slopes = {
    '>': (0,1),
    'v': (1,0),
    '<': (0,-1),
    '^': (-1,0)
}
def printMatrix():
    for row in matrix:
        print(''.join(row))

def getAdjecent(x, y, symb):
    adjecent = []
    if symb in slopes:
        dx, dy = slopes[symb]
        adjecent.append((x+dx, y+dy))
    else:
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            adjecent.append((x+dx, y+dy))
    return adjecent

def hike(loc, steps):
    global longest
    if loc[0] == len(matrix[0])-1:
        longest = max(longest, steps)
        return
    symbol = matrix[loc[0]][loc[1]]
    matrix[loc[0]][loc[1]] = 'O'
    for (x, y) in getAdjecent(*loc, symbol):
        if matrix[x][y] in '#O':
            continue
        hike((x,y), steps+1)
    matrix[loc[0]][loc[1]] = symbol

def getStart():
    for i, symb in enumerate(matrix[0]):
        if symb == '.':
            return (0, i)

printMatrix()
hike(getStart(), 0)
print("part1:", longest)




