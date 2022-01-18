# 152. Maximum Product Subarray


def maxProduct(nums):
	res = max(nums)
	curMin, curMax = 1, 1

	for n in nums:
		temp = n * curMax
		curMax = max(temp, n*curMin, n)
		curMin = max(temp, n*curMin, n)
		res = max(curMax, res)

	return res


if __name__ == '__main__':
	arr = [2,3,-2,4]
	ans = maxProduct(arr)
	print(ans)