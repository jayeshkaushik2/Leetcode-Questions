# 6020. Divide Array Into Equal Pairs

# time comp --> O(N) space comp --> O(N)
def divideArray(nums: list[int]) -> bool:
	hm = Counter(nums)
	for item in hm:
	    if hm[item] % 2 != 0:
	        return False
	
	return True

if __name__ == '__main__':
	nums = [3,2,3,2,2,2]
	res = divideArray(nums)
	print(res)