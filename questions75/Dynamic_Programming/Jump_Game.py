# 55. Jump Game

# time comp --> O(N) space comp --> O(1)
def canJump(nums):
	# reverse engineering
	n = len(nums)
	goal = n-1
	for i in range(n-2, -1, -1):
	    if (nums[i] + i) >= goal:
	        goal = i
	    
	return True if goal == 0 else False

if __name__ == '__main__':
	nums = [2,3,1,1,4]
	res = canJump(nums)
	print(res)