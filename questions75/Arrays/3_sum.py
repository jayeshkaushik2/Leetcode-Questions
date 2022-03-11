# 15. 3Sum

# tim comp --> O(N^2) space comp --> O(N)
def threeSum(nums):
	n = len(nums)
	nums.sort()
	res = []
	
	for i in range(n-2):
		if i == 0 or (nums[i] != nums[i-1]):
			target = 0 - nums[i]
			left  = i + 1
			right = n - 1

			while left < right:
				sumIs = nums[left] + nums[right]
				if sumIs == target:
					temp = [nums[i], nums[left], nums[right]]
					res.append(temp)

					while left < right and nums[left] == nums[left + 1]:
						left += 1
					while left < right and nums[right] == nums[right - 1]:
						right -= 1

					left += 1
					right -= 1
				elif sumIs > target:
					right -= 1
				else:
					left += 1

	return res

if __name__ == '__main__':
	nums = [-1,0,1,2,-1,-4]
	res = threeSum(nums)
	print(res)