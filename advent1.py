# import requests

# url = "https://adventofcode.com/2023/day/1/input"
# data = requests.get(url).text

# numbers = {
#     'one': 1,
#     'two': 2,
#     'three': 3,
#     'four': 4,
#     'five': 5,
#     'six': 6,
#     'seven': 7,
#     'eight': 8,
#     'nine': 9
# }

# trie = {}
# rev_trie = {}

# def addWord(node, word, num):
#   for c in word:
#       if c not in node:
#           node[c] = {}
#       node = node[c]
#   node['#'] = num

# for word in numbers:
#   addWord(trie, word, numbers[word])
#   addWord(rev_trie, word[::-1], numbers[word])


# file = open("input2.txt", 'r')

# # print(trie)
# # print(rev_trie)
# total = 0
# for line in file:
#   cal = 0
#   node = trie
#   for c in line:
#       if c.isdigit():
#           cal = int(c)*10
#           break
#       if c not in node:
#           node = trie
#       if c in node:
#           node = node[c]
#       if '#' in node:
#           cal = node['#']*10
#           break
#   node = rev_trie
#   for c in line[::-1]:
#       if c.isdigit():
#           cal += int(c)
#           break
#       if c not in node:
#           node = rev_trie
#       if c in node:
#           node = node[c]
#       if '#' in node:
#           cal += node['#']
#           break
#   print(line + " -> " + str(cal))
#   total += cal
# print(total)



import re

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

with open("input2.txt") as file:
    text = file.read()
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
    print(total)
