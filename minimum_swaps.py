# minimum swaps required to group all 1's together
nums = [0,1,0,1,1,0,0]

def minSwaps(nums: list[int]) -> int:
    n = len(nums)
    ones = nums.count(1)

    # since nums array is in cyclic manner that is why we do nums = nums+nums
    nums = nums+nums
    prefix = [0]
    for x in nums:
        prefix.append(prefix[-1] + x)
    
    best = 0
    print(prefix, nums)
    for i in range(n):
        best  = max(best, prefix[i+ones] - prefix[i])

    return ones - best

ans = minSwaps(nums)
print(ans)