# 1. Two Sum

# time comp --> O(N) space comp --> O(1)
def twoSum(nums: list[int], target: int) -> list[int]:
	n = len(nums)
	hm = {}
	res = [-1,-1]
	
	for i in range(n):
		n1 = nums[i]
		n2 = target - n1
		
		if n2 in hm:
			res[0] = hm[n2]
			res[1] = i
			break

		hm[n1] = i

	return res

if __name__ == '__main__':
	nums = [2,7,11,15]
	target = 9
	ans = twoSum(nums, target)
	print(ans)