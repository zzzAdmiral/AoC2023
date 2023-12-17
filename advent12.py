import sys

f = "input.txt"
if 1 < len(sys.argv):
	f = "input" + sys.argv[1] + ".txt"
file = open(f)

total = 0

def backtrack(record, nums, i, damaged, n, treatAs):
	if i == len(record):
		if (n == len(nums) and damaged == 0) or (n == len(nums)-1 and nums[n] == damaged):
			global total
			total += 1
		return
	if record[i] == '#' or treatAs == '#':
		backtrack(record, nums, i+1, damaged+1, n, '')
	elif record[i] == '.' or treatAs == '.':
		if damaged:
			if n == len(nums) or damaged != nums[n]:
				return
			n += 1
		backtrack(record, nums, i+1, 0, n, '')
	elif record[i] == '?':
		backtrack(record, nums, i, damaged, n, '#')
		backtrack(record, nums, i, damaged, n, '.')



# for line in file:
# 	record, nums = line.split()
# 	nums = list(map(int, nums.split(',')))
# 	backtrack(record, nums, 0, 0, 0, '')
# print(total)

for line in file:
	record, nums = line.split()
	nums = list(map(int, nums.split(',')))
	record = '?'.join([record] * 5)
	nums = nums * 5
	backtrack(record, nums, 0, 0, 0, '')
print(total)