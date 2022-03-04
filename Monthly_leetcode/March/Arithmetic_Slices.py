# 413. Arithmetic Slices

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
	# using extra space
	# time comp --> O(N) space comp --> O(N)
	n = len(nums)
	dp = [None]*(n-1)

	# storing all the differences of the elements of the nums in dp
	for i in range(1, n):
		dp[i-1] = nums[i] - nums[i-1]

	res = 0
	m = 1
	# checking for the equal diffrences in the dp
	for i in range(1, len(dp)):
		if dp[i] == dp[i-1]:
			res += m
			m += 1
		else:
			m = 1

	return res


	# time comp --> O(N^2) space comp --> O(1)
	n = len(nums)
	res = 0
	
	for i in range(1, n-1):
	    prev = nums[i-1]
	    present = nums[i]
	    diff = present - prev
	    prev = present
	    cnt = 2
	    
	    for j in range(i+1, n):
	        if nums[j]-prev == diff:
	            cnt += 1
	            prev = nums[j]
	        elif nums[j]-prev != diff:
	            break
	        if cnt > 2: res += 1
	    
	return res

if __name__ == '__main__':
	nums = [1,2,3,4]
	res = 
	print(res)