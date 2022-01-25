# 5990. Find All Lonely Numbers in the Array

# time comp --> O(N) space comp --> O(N)
from collections import Counter
def findLonely(nums: list[int]) -> list[int]:
	hm = Counter(nums)
	res = []

	for item in hm:
		if hm[item] == 1 and item+1 not in hm and item-1 not in hm:
			res.append(item)

	return res

if __name__ == '__main__':
	nums = [10,6,5,8]
	res = findLonely(nums)
	print(res)