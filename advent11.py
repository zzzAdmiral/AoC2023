import sys

f = "input.txt"
if 1 < len(sys.argv):
	f = "input" + sys.argv[1] + ".txt"
file = open(f)
matrix = [line.strip() for line in file]

m, n = len(matrix), len(matrix[0])
emptyRows = set()
emptyCols = set(range(n))
galaxies = []
for i in range(m):
	empty = True
	for j in range(n):
		if matrix[i][j] == '#':
			galaxies.append((i, j))
			if j in emptyCols:
				emptyCols.remove(j)
			empty = False
	if empty:
		emptyRows.add(i)


def shortestPath(g1, g2, expansion):
	(row1, row2) = (g1[0], g2[0]) if g1[0] < g2[0] else (g2[0], g1[0])
	(col1, col2) = (g1[1], g2[1]) if g1[1] < g2[1] else (g2[1], g1[1])
	dist = (row2 - row1) + (col2 - col1)
	for n in range(row1+1, row2):
		if n in emptyRows:
			dist += expansion - 1
	for n in range(col1+1, col2):
		if n in emptyCols:
			dist += expansion - 1
	return dist

def part1():
	total = 0
	for i, g1 in enumerate(galaxies):
		for g2 in galaxies[i+1:]:
			total += shortestPath(g1, g2, 2)
	return total

def part2():
	total = 0
	for i, g1 in enumerate(galaxies):
		for g2 in galaxies[i+1:]:
			total += shortestPath(g1, g2, 1000000)
	return total

print(part1())
print(part2())