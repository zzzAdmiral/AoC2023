import sys
import re

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"

XLow = 0
YLow = 1
ZLow = 2
XHi = 3
YHi = 4
ZHi = 5
SUPPORTS = 6
SUPPORTED_BY = 7

bricks = []
for line in open(f):
    nums = re.findall('\d+', line)
    nums = list(map(int, nums))
    nums.append([])
    nums.append([])
    bricks.append(nums)

bricks = sorted(bricks, key=lambda brick: brick[ZLow])

fallenBricks = []
for i, brick in enumerate(bricks):
    landedHeight = 1
    for fallenBrick in fallenBricks[::-1]:
        # if brick[ZLow] <= fallenBrick[ZHi]:
        #     continue
        if landedHeight > fallenBrick[ZHi] + 1:
            break
        if (brick[XLow] <= fallenBrick[XLow] <= brick[XHi]) or (fallenBrick[XLow] <= brick[XLow] <= fallenBrick[XHi]):
            if (brick[YLow] <= fallenBrick[YLow] <= brick[YHi]) or (fallenBrick[YLow] <= brick[YLow] <= fallenBrick[YHi]):
                landedHeight = fallenBrick[ZHi] + 1
                fallenBrick[SUPPORTS].append(i)
        

    fallDist = brick[ZLow] - landedHeight
    brick[ZLow] = landedHeight
    brick[ZHi] = brick[ZHi] - fallDist

    insertAt = len(fallenBricks)
    for fallenBrick in fallenBricks:
        if brick[ZHi] >= fallenBrick[ZHi]:
            break
        insertAt -= 1
    fallenBricks.insert(i, brick)


for i, brick in enumerate(bricks):
    for above in brick[SUPPORTS]:
        bricks[above][SUPPORTED_BY].append(i)

count = 0
for brick in bricks:
    disintagratable = True
    for above in brick[SUPPORTS]:
        if len(bricks[above][SUPPORTED_BY]) == 1:
            disintagratable = False
            break
    if disintagratable:
        count += 1

# print(bricks)
print(count) # 452 < x < 534





