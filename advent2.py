import re
import sys

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

def part1(n, groups):
	bag = {'red': 12, 'green': 13, 'blue': 14}

	for group in groups[1:]:
		cubes = group.split()
		while cubes:
			color = cubes.pop()
			num = int(cubes.pop())
			if bag[color] < num:
				return 0
	return n

def part2(groups):
	needed = {'red': 0, 'green': 0, 'blue': 0}
	for group in groups[1:]:
		cubes = group.split()
		while cubes:
			color = cubes.pop()
			num = int(cubes.pop())
			needed[color] = max(needed[color], num)
	return needed['red'] * needed['green'] * needed['blue']

with open(f) as file:
	total1 = 0
	total2 = 0
	n = 1
	for line in file:
		line = line.replace(',', '')
		groups = re.split(r"[;|:]", line)
		total1 += part1(n, groups)
		total2 += part2(groups)
		n += 1
	print("part1:", total1)
	print("part2:", total2)



