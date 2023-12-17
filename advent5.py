import re
import sys

f = "input.txt"
if 1 < len(sys.argv):
	f = "input" + sys.argv[1] + ".txt"

def parseConverter(group):
	converter = []
	for line in group.split('\n')[1:]:
		dest, source, rng = map(int, line.split())
		converter.append((dest, source, rng))
	return converter

# setup
with open(f) as file:
	text = file.read()
	groups = text.split('\n\n')
	converters = []
	for group in groups[1:]:
		converters.append(parseConverter(group))
	seeds = list(map(int, groups[0].split()[1:]))

conversionTypes = ["seed", "soil", "fertilizer", "water", "light", "temp", "humidity", "location"]

def seedToLocation(val):
	for converter in converters:
		for dest, source, rng in converter:
			if source <= val < source+rng:
				val = dest + (val-source)
				break
	return val

def part1():
	smallest = float('inf')
	for val in seeds:
		smallest = min(smallest, seedToLocation(val))
	return smallest


def reverseConversion(inTuple, converter, printMe=False):
	searchStart, searchRng = inTuple
	while searchRng > 0:
		found = False
		# check list range for searchStart
		for dest, source, rng in converter:
			if dest <= searchStart <= dest+rng-1:
				offset = searchStart - dest
				leftoverRng = rng - offset
				usedRng = min(leftoverRng, searchRng)
				yield source+offset, usedRng
				searchRng -= usedRng
				searchStart += usedRng
				found = True
				break
		# searchStart is unlisted
		if not found:
			possibleNextDest = [tup[0] for tup in converter if tup[0] > searchStart]
			if possibleNextDest:
				nextDest = min(possibleNextDest)
				leftoverRng = nextDest - searchStart
				usedRng = min(leftoverRng, searchRng)
				yield searchStart, usedRng
				searchRng -= usedRng
				searchStart += usedRng
			else:
				yield searchStart, searchRng
				searchRng = 0

def seedExists(valStart, valRng):
	for i in range(0, len(seeds), 2):
		seedStart = seeds[i]
		seedRng = seeds[i+1]
		if valStart <= seedStart < (valStart + valRng):
			return seedStart
		elif seedStart <= valStart < (seedStart + seedRng):
			return valStart
	return None

def recursiveConversion(inTuple, i):
	if i < 0:
		if seed := seedExists(inTuple[0], inTuple[1]):
			return seed
		return False
	for outTuple in reverseConversion(inTuple, converters[i]):
		if res := recursiveConversion(outTuple, i-1):
			return res

def part2():
	locs = sorted(converters[-1], key = lambda tup: tup[0], reverse=True)
	nextStartLoc = 0
	while locs:
		listedLocation = locs[-1][0]
		if nextStartLoc == listedLocation:
			rng = locs.pop()[2]
		else:
			rng = listedLocation - nextStartLoc
		if foundSeed := recursiveConversion((nextStartLoc, rng), 6):
			print("found seed!", foundSeed)
			return seedToLocation(foundSeed)
		nextStartLoc = nextStartLoc + rng


print("part 1:", part1())
print("part 2:", part2())