
import sys
from math import floor

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

def winningWays(time, distance):
	quad_min = (-time + (time ** 2 - 4 * distance) ** 0.5) / (2 * -1)
	quad_max = (-time - (time ** 2 - 4 * distance) ** 0.5) / (2 * -1)
	if quad_min % 1 == 0:
		return floor(quad_max) - floor(quad_min) - 1
	return floor(quad_max) - floor(quad_min)


# setup
file = open(f)
text = file.read()
lines = text.split('\n')
times = lines[0].split()[1:]
distances = lines[1].split()[1:]

def part1(times, distances):
	val = 1
	for i in range(len(times)):
		ways = winningWays(int(times[i]), int(distances[i]))
		val *= ways
	return val

def part2(times, distances):
	time = ''.join(times)
	distance = ''.join(distances)
	return winningWays(int(time), int(distance))

print("part1:", part1(times, distances))
print("part2:", part2(times, distances))
