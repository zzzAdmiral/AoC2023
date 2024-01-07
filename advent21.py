import sys

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

matrix = [list(line.strip()) for line in open(f)]

def findStart():
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == 'S':
                return (i, j)

def neighbors(starts):
    reachable = set()
    for start in starts:
        for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            x, y = start[0]+dx, start[1]+dy
            if matrix[x][y] != '#':
                reachable.add((x,y))
    return reachable


def part1():
    gardens = {findStart()}
    seq = []
    for i in range(64):
        gardens = neighbors(gardens)
        if i % 2 == 1:
            seq.append(len(gardens))
    print(seq)
    return len(gardens)

print("part1:", part1())