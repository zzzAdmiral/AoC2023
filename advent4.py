import re
import sys

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

def getMatches(line):
	start = line.index(':')
	groups = line[start+1:].split('|')
	winners = groups[0].split()
	numbers = groups[1].split()
	count = 0
	for num in numbers:
		if num in winners:
			count += 1
	return count

def part1():
	with open(f) as file:
		total = 0
		for line in file:
			c = getMatches(line)
			if c > 0:
				total += 2**(c-1)
		return total

def part2():
	count = []
	with open(f) as file:
		for line in file:
			count.append(getMatches(line))

	scratchcards = [1] * len(count)
	for idx in range(len(scratchcards)-1, -1, -1):
		for n in range(1, count[idx]+1):
			scratchcards[idx] += scratchcards[idx+n]
	return sum(scratchcards)

print("part1:", part1())
print("part2:", part2())