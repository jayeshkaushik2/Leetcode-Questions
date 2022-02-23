# 2176. Count Equal and Divisible Pairs in an Array

# time comp --> O(N^2) sapce comp --> O(1)
def countPairs(nums: list[int], k: int) -> int:
	n = len(nums)
	res = 0
	for i in range(n):
	    for j in range(i+1, n):
	        if nums[i] == nums[j] and (i*j) % k == 0:
	            res += 1
	
	return res

if __name__ == '__main__':
	nums = [3,1,2,2,2,1,3]
	k = 2
	res = countPairs(nums, k)
	print(res)