# 152. Maximum Product Subarray

def maxProduct(nums):
	# time comp --> O(N) space comp --> O(1)
	res = max(nums)
	curMax, curMin = 1, 1

	for ele in nums:
		temp = curMax*ele
		curMax = max(curMax*ele, curMin*ele, ele)
		curMin = min(temp, curMin*ele, ele)
		res = max(curMax, res)

	return res
	
	
	'''
	brute force solution is to calculate each subarray product and find the maximum
	time comp --> O(N^2) space comp --> O(N)
	'''
	maxProduct = 0
	for i in range(len(nums)):
	    product = nums[i]
	    for j in range(i+1, len(nums)):
	        maxProduct = max(maxProduct, product)
	        product *= nums[j]
	    maxProduct = max(maxProduct, product)
	
	return maxProduct


if __name__ == '__main__':
	nums = [2,3, -2, 4]
	res = maxProduct(nums)
	print(res)