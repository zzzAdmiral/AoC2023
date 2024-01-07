import sys
import re
from copy import copy

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

file = open(f).read()
wf, p = file.split('\n\n')
wf = wf.split('\n')
workflows = {}
for line in wf:
    start = line.index('{')
    name = line[:start]
    workflows[name] = line[start+1:-1].split(',')
p = p.split('\n')
parts = []
for line in p:
    nums = re.findall('\d+', line)
    parts.append(list(map(int, nums)))

def part1(parts, workflows):
    accepted = []
    for part in parts:
        x, m, a, s = part
        workflow = workflows['in']
        done = False
        while not done:
            name = None
            for rule in workflow:
                sep = rule.split(':')
                if len(sep) == 1:
                    name = sep[0]
                if len(sep) == 2:
                    if eval(sep[0]):
                        name = sep[1]
                if name:
                    if name == 'R':
                        done = True
                    elif name == 'A':
                        accepted.append(part)
                        done = True
                    else:
                        workflow = workflows[name]
                    break
    total = 0
    for part in accepted:
        total += sum(part)
    return total

valid = []
def aux(name, ranges):
    if name == 'A':
        valid.append(ranges)
        return
    elif name == 'R':
        return
    for rule in workflows[name]:
        sep = rule.split(':')
        if len(sep) == 1:
            aux(sep[0], ranges)
        elif len(sep) == 2:
            i = "xmas".index(sep[0][0])
            sign = sep[0][1]
            val = int(sep[0][2:])
            newRanges = copy(ranges)
            low, high = ranges[i]
            if sign == "<": #a<2006:qkq
                if low >= val:
                    continue
                newRanges[i] = (low, val-1)
                ranges[i] = (val, high)
            elif sign == ">":
                if high <= val:
                    continue
                newRanges[i] = (val+1, high)
                ranges[i] = (low, val)
            aux(sep[1], newRanges)



def part2():
    aux("in", [(1, 4000)] * 4)
    total = 0
    for ranges in valid:
        # print(ranges)
        mult = 1
        for low, high in ranges:
            mult *= (high-low+1)
        total += mult
    return total


print("part1:", part1(parts, workflows))
print("part2:", part2())