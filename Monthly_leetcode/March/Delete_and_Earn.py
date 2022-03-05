# 740. Delete and Earn

# time comp --> O(N) space comp --> O(N)
def deleteAndEarn(nums: list[int]) -> int:
	hm = Counter(nums)
	nums = sorted(list(set(nums)))
	
	earn1 = earn2 = 0
	for i in range(len(nums)):
	    # calculating the total number of nums[i]s we have
	    curEarn = nums[i] * hm[nums[i]]
	    if i > 0 and nums[i] == nums[i-1] + 1:
	        temp = earn2 
	        earn2 = max(curEarn + earn1, earn2)
	        earn1 = temp
	    else:
	        temp = earn2
	        earn2 = curEarn + earn2
	        earn1 = temp
	
	return earn2


if __name__ == '__main__':
	nums = [3,4,2,3,3,3]
	res = deleteAndEarn(nums)
	print(res)