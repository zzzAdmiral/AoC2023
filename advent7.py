import sys
from collections import Counter
import functools

f = "input.txt"
if 1 < len(sys.argv):
	f = "input" + sys.argv[1] + ".txt"

types = ["High card", "One pair", "Two pair", "Three of a kind", "Full house", "Four of a kind", "Five of a kind"]
# cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 0, 'T': 10}
for n in range(1, 10):
	cards[str(n)] = n

def handType(hand):
	noJHand = [c for c in hand if c != 'J']
	counter = sorted(Counter(noJHand).values(), reverse=True)
	jokers = hand.count('J')
	if jokers == 5:
		return 6
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
	print("these hands aren't unique!", hands1)
	return 0

with open(f) as file:
	allHands = []
	for line in file:
		hand, bid = line.split()
		allHands.append((hand, bid))
	print(cards)
	allHands = sorted(allHands, key=functools.cmp_to_key(compare))
	total = 0
	i = 1
	for _, bid in allHands:
		total += int(bid)*i
		i += 1
	print(total)
#249511092