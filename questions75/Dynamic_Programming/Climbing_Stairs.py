# 70. Climbing Stairs

def climbStairs(n):
	# rescursion -- > O(2**N) space comp --> O(1)
	def cnt(i):
	    if i == 0: return 1
	    if i < 0: return 0
	    
	    c1 = cnt(i-1)
	    c2 = cnt(i-2)
	    return c1 + c2
        
	return cnt(n)
	
	
	
	# memoization --> O(N) space comp ==> O(N)
	def cnt(i, dp):
	    if i == 0: return 1
	    if i < 0: return 0
	    
	    if dp[i] != -1:
	        return dp[i]
	    
	    c1 = cnt(i-1, dp)
	    c2 = cnt(i-2, dp)
	    dp[i] = c1 + c2
	    
	    return dp[i]
	    
	dp = [-1] * (n+1)
	res = cnt(n, dp)
	return res
    
    
	    
	# bottom up approach --> O(N) space comp --> O(N) 
	if n == 1:
	    return 1
	nums = [0] * (n + 1)
	nums[1] = nums[0] = 1
	
	for i in range(2, n+1):
	    nums[i] = nums[i-1] + nums[i-2]
	
	return nums[n]
    
    
    
	# space optimization --> O(N) space comp --> O(1)
	def cnt(i):
	    if i == 1 or i == 0:
	        return 1
	    
	    a, b  = 1, 1
	    for j in range(2, i + 1):
	        c = a + b
	        a = b
	        b = c
	    
	    return c
	        
	return cnt(n)

if __name__ == '__main__':
	n = 25
	res = climbStairs(n)
	print(res)