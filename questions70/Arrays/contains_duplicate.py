# 217. Contains Duplicate

 # time comp --> O(N) space comp -->O(N)
def containsDuplicate(nums):
	hm = {}
	n = len(nums)

	for i in range(n):
		if nums[i] in hm:
			return True
		hm[nums[i]] = 1

	return False


if __name__ == '__main__':
	nums = [1,2,3,1]
	ans = containsDuplicate(nums)
	print(ans)