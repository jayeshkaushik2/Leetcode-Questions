# 53. Maximum Subarray

# time comp --> O(N) space comp --> O(1)
def maxSubArray(nums: list[int]) -> int:
	n = len(nums)
	curSum = nums[0]
	maxSum = nums[0]

	for i in range(1, n):
		if curSum >= 0:
			curSum += nums[i]
		else:
			curSum = nums[i]

		if curSum > maxSum:
			maxSum = curSum

	return maxSum


if __name__ == '__main__':
	nums = [-2,1,-3,4,-1,2,1,-5,4]
	ans = maxSubArray(nums)
	print(ans)