# 1752. Check if Array Is Sorted and Rotated

# time comp --> O(N) space comp --> O(1)
def check(nums):
    cnt = 0
    n = len(nums)
    for i in range(1, n):
        if nums[i] < nums[i-1]:
            cnt += 1
    
    if nums[-1] > nums[0]:
        cnt += 1
    
    return cnt <= 1

if __name__ == '__main__':
	nums = [3,4,5,1,2]
	res = check(nums)
	print(res)