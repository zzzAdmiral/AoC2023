import sys

f = "inputs/input.txt"
if 1 < len(sys.argv):
    f = "inputs/input" + sys.argv[1] + ".txt"
file = open(f)

str2num = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

def replace_words(text):
    for k, v in str2num.items():
        text = text.replace(k, v)
    return text

def calibrate(use_words=False):
    with open(f) as file:
        text = file.read()
        if use_words:
            text = replace_words(text)
        total = 0
        for line in text.split("\n"):
            cal = 0
            for c in line:
                if c.isdigit():
                    cal = int(c)*10
                    break
            for c in line[::-1]:
                if c.isdigit():
                    cal += int(c)
                    break
            total += cal
        return total

print("part1: ", calibrate())
print("part2: ", calibrate(True))
