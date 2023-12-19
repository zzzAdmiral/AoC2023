import sys
import copy

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

def printMatrix(matrix):
    for row in matrix:
        print(row)
    print('\n\n')

def calculateWeight(matrix):
    m = len(matrix)
    total = 0
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == 'O':
                total += m-i
    return total

def northSouth(matrix, north):
    tilted = []
    for j, col in enumerate(zip(*matrix)):
        col = ''.join(col)
        gaps = col.split('#')
        updated_col = []
        for gap in gaps:
            gap = sorted(gap, reverse=north)
            updated_col.append(''.join(gap))
        updated_col = '#'.join(updated_col)
        # print(updated_col)
        # for i, c in enumerate(updated_col):
            # print("%s -> %s" % ( matrix[i][j], c))
            # matrix[i][j] = c
        tilted.append(updated_col)
    tilted = zip(*tilted)    
    for i, row in enumerate(tilted):
        matrix[i] = ''.join(row)
    return matrix

def eastWest(matrix, west):
    for i, row in enumerate(matrix):
        # row = ''.join(row)
        gaps = row.split('#')
        updated_row = []
        for gap in gaps:
            gap = sorted(gap, reverse=west)
            updated_row.append(''.join(gap))
        updated_row = '#'.join(updated_row)
        matrix[i] = updated_row
    return matrix


def cycle(matrix, n):
    weights = [0]
    ms = []
    for i in range(n):
        # print(i)
        matrix = northSouth(matrix, True)
        matrix= eastWest(matrix, True)
        matrix = northSouth(matrix, False)
        matrix= eastWest(matrix, False)
        # printMatrix(matrix)
        weights.append(calculateWeight(matrix))
    return weights

def part1(matrix):
    matrix = northSouth(matrix, True)
    return calculateWeight(matrix)

def part2(matrix):
    n = 1000
    cycleWeights = cycle(matrix, n)
    # [114, 142, 192, 220, 270, 298, 348, 376, 426, 454, 504, 532, 582, 610, 660, 688, 738, 766, 816, 844, 894, 922, 972, 1000]
    indices = [i for i, x in enumerate(cycleWeights) if x == cycleWeights[-1]]
    # 28
    cycleLength = indices[-1] - indices[-2]
    # [96446, 96474, 96464, 96471, 96461, 96485, 96501, 96517, 96472, 96455, 96436, 96454, 96452, 96464, 96450, 96461, 96454, 96482, 96490, 96519, 96493, 96469, 96438, 96457, 96459, 96470, 96440, 96447]
    repeating = cycleWeights[n - cycleLength:]
    i = (1000000000 - n) % cycleLength
    return repeating[i]

file = open(f)
matrix = [line.strip() for line in file]
print("part1:", part1(copy.copy(matrix)))
print("part2:", part2(matrix))