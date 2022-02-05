# 594. Longest Harmonious Subsequence
from collections import Counter

# time comp --> O(N) space comp --> O(N)
def findLHS(nums):
	res = 0
	n = len(nums)
	hm = Counter(nums)
	nums.sort()
	
	for temp in hm:
	    cnt = hm[temp]
	    flag = False
	    if temp+1 in hm:
	        flag = True
	        cnt += hm[temp+1]
	    if flag:
	        res = max(res, cnt)
	        
	return res



if __name__ == '__main__':
	nums = [1,3,2,2,5,2,3,7]
	res = findLHS(nums)
	print(res)