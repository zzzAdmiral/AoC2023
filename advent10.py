import sys

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"
file = open(f)
matrix = [list(line.strip()) for line in file]

path = []
groups = [[],[]]
groupings = []


NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

# N E S W
adjacent = [(-1, 0), (0, 1), (1, 0), (0, -1)]
possible = {
	'S': ['|7F', '-J7', '|LJ', '-LF'],
	'|': ['S|7F', '', 'S|LJ', ''],
	'-': ['', 'S-J7', '', 'S-LF'],
	'L': ['S|7F', 'S-J7', '', ''],
	'J': ['S|7F', '', '', 'S-LF'],
	'7': ['', '', 'S|LJ', 'S-LF'],
	'F': ['', 'S-J7', 'S|LJ', '']
}

turns = {
	'L': {NORTH: EAST, EAST: NORTH, SOUTH: WEST, WEST: SOUTH},
	'J': {NORTH: WEST, EAST: SOUTH, SOUTH: EAST, WEST: NORTH},
	'7': {NORTH: EAST, EAST: NORTH, SOUTH: WEST, WEST: SOUTH},
	'F': {NORTH: WEST, EAST: SOUTH, SOUTH: EAST, WEST: NORTH}
}

def printMatrix():
	for row in matrix:
		print(''.join(row))

def findStart():
	for i, row in enumerate(matrix):
		for j, c in enumerate(row):
			if c == 'S':
				return (i, j)

def getSymbol(tup):
	return matrix[tup[0]][tup[1]]

def getPath():
	start = findStart()
	prev, loc = start, start
	count = 0
	path = []
	while True:
		path.append(loc)
		count += 1
		symb = getSymbol(loc)
		for direction, (dx, dy) in enumerate(adjacent):
			x, y = loc[0]+dx, loc[1]+dy

			# out of range
			if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
				continue

			if matrix[x][y] in possible[symb][direction] and (x, y) != prev:
				if (x, y) == start:
					return path
				prev = loc
				loc = (x, y)
				break

def updateGroupings(node):
	symb = getSymbol(node)
	for i in [0, 1]:
		groupings[i] = turns[symb][groupings[i]]


def findOutsiders(node):
	for i in [0,1]:
		dx, dy = adjacent[groupings[i]]
		x, y = node[0] + dx, node[1] + dy
		if (x,y) not in path and getSymbol((x,y)) not in '01mS':
			markNode((x,y), i)
			groups[i].append((x,y))

def markNode(tup, mark):
	matrix[tup[0]][tup[1]] = str(mark)

def markNeighbors(i):
	group = groups[i]
	count = 0
	while group:
		x, y = group.pop()
		count += 1
		if x <= 0 or y <= 0 or x >= len(matrix)-1 or y >= len(matrix[0])-1:
			return 0
		for dx, dy in adjacent:
			node = (x+dx, y+dy)
			if getSymbol(node) not in '01mS':
				group.append(node)
				markNode(node, i)
	return count


def part2():
	for direction, possiblities in enumerate(possible[getSymbol(path[1])]):
		if not possiblities:
			groupings.append(direction)

	for node in path[1:]:
		findOutsiders(node)
		if getSymbol(node) in turns:
			updateGroupings(node)
			findOutsiders(node)
		markNode(node, 'm')

	# printMatrix()
	return markNeighbors(0) or markNeighbors(1)

path = getPath()
print("part1: ", len(path) // 2)
# Wow this is slow!
print("part2: ", part2())
