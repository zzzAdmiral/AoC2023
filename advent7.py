import sys
from collections import Counter
import functools

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

types = ["High card", "One pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind"]
cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
for n in range(1, 10):
	cards[str(n)] = n

def handType(hand):
	counter = Counter(hand)
	jokers = 0
	# if Js are jokers
	if cards['J'] == 0:
		jokers = counter['J']
		if jokers == 5:
			return 6
		counter['J'] = 0
	counter = sorted(counter.values(), reverse=True)
	counter[0] += jokers
	if counter[0] == 5:
		return 6
	elif counter[0] == 4:
		return 5
	elif counter[0] == 3 and counter[1] == 2:
		return 4
	elif counter[0] == 3:
		return 3
	elif counter[0] == 2 and counter[1] == 2:
		return 2
	elif counter[0] == 2:
		return 1
	else:
		return 0

def compare(tup1, tup2):
	hand1, hand2 = tup1[0], tup2[0]
	t1, t2 = handType(hand1), handType(hand2)
	if t1 < t2:
		return -1
	elif t1 > t2:
		return 1
	for c1, c2 in zip(hand1, hand2):
		if c1 != c2:
			res = cards[c1] - cards[c2]
			return 1 if res > 0 else -1
	raise Exception("Hand %s isn't unique!" % hands1)




def winnings(allHands, use_jokers=False):
	cards['J'] = 0 if use_jokers else 11
	allHands = sorted(allHands, key=functools.cmp_to_key(compare))
	total = 0
	i = 1
	for _, bid in allHands:
		total += int(bid)*i
		i += 1
	return total


file = open(f)
allHands = []
for line in file:
	hand, bid = line.split()
	allHands.append((hand, bid))

print("part1:", winnings(allHands, False))
print("part2:", winnings(allHands, True))

