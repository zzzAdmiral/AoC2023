import re
import sys

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

def part1(numbers, symbols):
	total = 0
	for i, row in enumerate(numbers):
		for start, end, num in row:
			valid = False
			# check same row
			if start-1 in symbols[i] or end+1 in symbols[i]:
				valid = True
			# check above
			if not valid and i > 0:
				for j in symbols[i-1]:
					if start-1 <= j <= end+1:
						valid = True
						break
			# check below
			if not valid and i < len(symbols)-1:
				for j in symbols[i+1]:
					if start-1 <= j <= end+1:
						valid = True
						break
			if valid:
				total += num
	return total


def part2(numbers, gears):
	total = 0
	for i, row in enumerate(gears):
		for j in row:
			adj = []
			# check same row
			for start, end, num in numbers[i]:
				if start-1 <= j <= end+1:
					adj.append(num)
			# check above
			if i > 0:
				for start, end, num in numbers[i-1]:
					if start-1 <= j <= end+1:
						adj.append(num)
			# check below
			if i < len(gears) - 1:
				for start, end, num in numbers[i+1]:
					if start-1 <= j <= end+1:
						adj.append(num)
			if len(adj) == 2:
				total += adj[0] * adj[1]
	return total


with open(f) as file:
	symbols = []
	numbers = []
	gears = []
	for line in file:
		symbols.append(set())
		numbers.append(set())
		gears.append(set())
		num = None
		start = None
		i = 0
		for c in line:
			if c.isdigit():
				if not num:
					start = i
					num = int(c)
				else:
					num = num*10 + int(c)
			elif num:
				numbers[-1].add((start, i-1, num))
				num = None
			if c == '*':
				gears[-1].add(i)
			if c == '\n':
				break
			elif c != '.' and not c.isdigit() and not c.isalnum():
				symbols[-1].add(i)
			i += 1
		if num:
			numbers[-1].add((start, i-1, num))

print("part1:", part1(numbers, symbols))
print("part2:", part2(numbers, gears))