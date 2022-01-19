# 153. Find Minimum in Rotated Sorted Array

# time comp --> O(log(N)) space comp --> O(1)
def findMin(nums: list[int]) -> int:
	n = len(nums)
	l, r = 0, n-1
	res = nums[0]

	while l <= r:
		# the array is sorted
		if nums[l] < nums[r]:
			res = min(res, nums[l])
			break

		m = l + (r-l)//2
		res = min(res, nums[m])

		if nums[m] >= nums[l]:
			# means we are in the left part --> we have to search in right part
			l = m + 1
		else:
			r = m - 1

	return res




if __name__ == '__main__':
	nums = [3,4,5,1,2]
	res = findMin(nums)
	print(res)