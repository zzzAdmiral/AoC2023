import sys

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

def printRowflection(matrix, n):
	for i, line in enumerate(matrix):
		if i == n-1:
			print('>' + line)
		else:
			print(' ' + line)

def printColflection(matrix, n):
	for line in matrix:
		print(line)
	print(' '*(n-1) + '^')

def findDiff(m1, m2):
	count = 0
	for a,b in zip(m1, m2):
		if a != b:
			count += 1
	return count

def compareSlices(m1, m2, smudge):
	size = min(len(m1), len(m2))
	for i in range(size):
		smudge -= findDiff(m1[-(i+1)], m2[i])
		if smudge < 0:
			return False
	return smudge ==  0


def findReflection(matrix, smudge):
	for i, row in enumerate(matrix):
		if i < len(matrix)-1 and findDiff(matrix[i], matrix[i+1]) <= smudge:
			if compareSlices(matrix[:i+1], matrix[i+1:], smudge):
				return i+1
		# Apperantly there can't be a middle line between reflections...
		# if i < len(matrix)-2 and findDiff(matrix[i], matrix[i+2]) <= smudge:
		# 	if compareSlices(matrix[:i+1], matrix[i+2:], smudge):
		# 		return i+1


def solve(smudge):
	file = open(f)
	mirrors = file.read().split('\n\n')
	total = 0
	for mirror in mirrors:
		matrix = [line.strip() for line in mirror.split('\n')]
		if n := findReflection(matrix, smudge):
			# printRowflection(matrix, n)
			total += n*100
		else:
			flipped = list(zip(*matrix[::-1]))
			n = findReflection(flipped, smudge)
			# printColflection(matrix, n)
			total += n
		# print('\n')

	return total

print("part1:", solve(0))
print("part2:", solve(1))
