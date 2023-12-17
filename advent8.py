import re
import sys
import math

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

instructions = ""
network = {}
with open(f) as file:
	for line in file:
		if not instructions:
			instructions = line.strip()
			continue
		if line.isspace():
			continue
		locs = re.findall(r'(\w+)', line)
		network[locs[0]] = (locs[1], locs[2])

def part1():
	count = 0
	loc = "AAA"
	while True:
		for c in instructions:
			if c == "L":
				loc = network[loc][0]
			elif c == "R":
				loc = network[loc][1]
			count += 1
			if loc == "ZZZ":
				return count

def part2():
	locs = [loc for loc in network.keys() if loc[-1] == 'A']
	cycles = []
	for loc in locs:
		count = 0
		while True:
			for i, c in enumerate(instructions):
				d = 0 if c == "L" else 1
				loc = network[loc][d]
			count += 1
			if loc[-1] == 'Z':
				cycles.append(count)
				break
	return len(instructions) * math.lcm(*cycles)

print("part1:", part1())
print("part2:", part2())