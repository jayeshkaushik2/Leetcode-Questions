# 5989. Count Elements With Strictly Smaller and Greater Elements

# time comp --> O(N) space comp --> O(1)
def countElements(nums: list[int]) -> int:
	ans = 0
	n = len(nums)

	for i in range(1, n-1):
		if nums[i] > 0 and nums[i] < nums[n-1]:
			ans += 1

	return ans

if __name__ == '__main__':
	nums = [11,7,2,15]
	res = countElements(nums)
	print(res)