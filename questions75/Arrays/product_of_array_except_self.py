# 238. Product of Array Except Self

# time comp --> O(N) space comp --> O(N) if you consider res array as a space
def productExceptSelf(nums):
	n = len(nums)
	res = [1]*n
	prefix = 1
	postfix = 1

	for i in range(n):
		res[i] = prefix
		prefix *= nums[i]

	for i in range(n-1, -1, -1):
		res[i] *= postfix
		postfix *= nums[i]

	return res

if __name__ == '__main__':
	arr = [1,2,3,4]
	ans = productExceptSelf(arr)
	print(ans)