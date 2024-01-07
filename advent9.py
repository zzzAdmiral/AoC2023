import sys

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"


def getNextNum(seq, part):
	allZeros = True
	nextSeq = []
	for i in range(1, len(seq)):
		nextSeq.append(seq[i]-seq[i-1])
		if seq[i] != 0:
			allZeros = False
	print(nextSeq)
	if allZeros:
		return 0
	if part == 1:
		return seq[-1] + getNextNum(nextSeq, part)
	elif part == 2:
		return seq[0] - getNextNum(nextSeq, part)

file = open(f)
total1 = 0
total2 = 0
for line in file:
	seq = list(map(int, line.split(', ')))
	total1 += getNextNum(seq, 1)

print("part1:", total1)
