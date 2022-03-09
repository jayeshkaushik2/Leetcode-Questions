# 1359. Count All Valid Pickup and Delivery Options

def countOrders(n: int) -> int:
	# time comp --> O(N) space comp --> O(1)
	# we can also do this without using the extra space
	mod = 10**9 + 7
	res = 1
	for i in range(2, n+1):
		'''
		formula is
		where 0 <= n <= N
		res x n(2n -1) % mod
		'''
		res = res * (2*i - 1) * (2*i)//2 % mod

	return res

	# time comp --> O(N) space comp --> O(N)
	# using the extra space comp
	mod = 10**9 + 7
	dp = [0]*(n+1)
	dp[0] = 1
	for i in range(1, n+1):
	    dp[i] = i*(dp[i-1])*(2*i - 1)
	    # we also have to mod with mod
	    dp[i] %= mod
	    
	return dp[n]


if __name__ == '__main__':
	n = 3
	res = countOrders(n)
	print(res)