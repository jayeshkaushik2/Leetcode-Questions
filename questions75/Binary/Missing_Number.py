# 268. Missing Number

# time comp --> O(N) space comp --> O(1)
def missingNumber(nums: list[int]) -> int:
	# get the original total sum of n numbers and get the sum of array element and ans is the difference
	n = len(nums)
	return n*(n+1)//2 - sum(nums)



	# n = 1
	# while n in nums:
	# 	n += 1
	# return n




if __name__ == '__main__':
	nums = [3,0,1]
	res = missingNumber(nums)
	print(res)