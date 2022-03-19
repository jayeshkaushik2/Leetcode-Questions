# 6022. Minimum Operations to Halve Array Sum

# time comp --> O(N) space comp --> O(N)
def halveArray(nums: list[int]) -> int:
    h = []
    
    for x in nums:
        heapq.heappush(h, -x)
        
    initial = sum(nums)
    current = initial
    steps = 0
    
    while current * 2 > initial:
        now = heapq.heappop(h)
        now = -now
        now /= 2
        
        current -= now
        heapq.heappush(h, -now)
        steps += 1
        
    return steps

if __name__ == '__main__':
    nums = 
    res = halveArray(nums)
    print(res)