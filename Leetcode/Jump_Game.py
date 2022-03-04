# 55. Jump Game

# time comp --> O(N) space comp --> O(1)
def canJump(self, nums):
	n = len(nums)
	goal = n-1
	
	for i in range(n-1, -1, -1):
	    if nums[i]+i >= goal:
	        goal = i
	
	return goal == 0


if __name__ == '__main__':
	nums = [2,3,1,1,4]
	res = 
	print(res)