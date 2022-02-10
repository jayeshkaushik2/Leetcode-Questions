# 560. Subarray Sum Equals K

def subarraySum(nums: list[int], k: int) -> int:
        
        # this is the brute force solution time comp --> O(N^2) space comp --> O(1)
#         n = len(nums)
#         res = 0
        
#         for i in range(n):
#             sumis = nums[i]
#             if sumis == k:
#                 res += 1
            
#             j = i+1
#             while j < n:
#                 sumis += nums[j]
#                 if sumis == k:
#                     res += 1
#                 j += 1
        
#         return res
        
        
        # I have to understand this
        # time comp --> O(N) space comp --> O(N)
        '''
		get the current sum
		find the difference between curSum and k
		check if it is present in the hashmap or not
		if True increment the value of res
		add the curSum + 1 to the hashmap
        '''
        res = 0
        curSum = 0
        prefSum = {0:1}
        
        for n in nums:
            curSum += n
            diff = curSum - k
            
            res += prefSum.get(diff, 0)
            prefSum[curSum] = 1 + prefSum.get(curSum, 0)
        
        return res

if __name__ == '__main__':
	nums = [1,1,1]
	res = subarraySum(nums)
	print(res)