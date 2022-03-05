# 6024. Most Frequent Number Following Key In an Array

# time comp --> O(N^2) space comp --> O(1)
def mostFrequent(nums: list[int], key: int) -> int:
	res = 0
	orcnt = 0
	for i in range(len(nums)-1):
	    cnt = 1
	    if nums[i] == key:
	        temp = nums[i+1]
	        for j in range(i+1, len(nums)-1):
	            if nums[j] == key and nums[j+1] == temp:
	                cnt += 1
	                
	        if cnt > orcnt:
	            orcnt = cnt
	            res = temp
	
	return res

if __name__ == '__main__':
	nums = [1,100,200,1,100]
	key = 1
	res = mostFrequent(nums, key)
	print(res)