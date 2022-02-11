# Top K Frequent Elements

# time comp --> O(N) space comp --> O(N)
from collections import Counter
def topKFrequent(nums, k):
	# counts of the elements
	hm = Counter(nums)
	freq = [[] for i in range(len(nums) + 1)]

	for ele, count in hm:
		freq[count].append(ele)

	res = []

	for i in range(len(freq)-1, 0, -1):
		for n in freq[i]:
			res.append(n)
			if len(res) == k:
				return res


if __name__ == '__main__':
	nums = [1,1,1,2,2,100]
	k = 2
	res =  topKFrequent(nums, k)
	print(res)