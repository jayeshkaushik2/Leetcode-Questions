# 238. Product of Array Except Self

# time comp --> O(N) space comp --> O(1)
def productExceptSelf(nums):
	'''
	nums = [1,2,3,4]

	calculate prefix = [1,2,6,24]
	calculate postfix = [24,24,12,4]

	res = [24, 12, 8, 6]
	'''
	n = len(nums)
	res = [1]*n
	
	prefix = 1
	for i in range(0, n):
	    res[i] *= prefix
	    prefix *= nums[i]
	
	postfix = 1
	for i in range(n-1, -1, -1):
	    res[i] *= postfix
	    postfix *= nums[i]
	
	return res

if __name__ == '__main__':
	nums = [1,2,3,4]
	res = productExceptSelf(nums)
	print(res)