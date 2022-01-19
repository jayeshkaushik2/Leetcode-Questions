# 33. Search in Rotated Sorted Array

# time comp --> O(log(N)) space comp --> O(1)
def search(nums: list[int], target: int) -> int:
	n = len(nums)
	l, r = 0, n-1

	while l <= r:
		m = l + (r-l)//2
		if nums[m] == target:
			return m

		# check if it is on left part or right
		if nums[m] >= nums[l]:
			# left part
			if nums[m] < target or nums[l] > target:
				l = m + 1
			else:
				r = m - 1
		else:
			if nums[m] > target or nums[r] < target:
				r = m - 1
			else:
				l = m + 1

	return -1


if __name__ == '__main__':
	nums = [4,5,6,7,0,1,2]
	target = 0
	res = search(nums, target)
	print(res)