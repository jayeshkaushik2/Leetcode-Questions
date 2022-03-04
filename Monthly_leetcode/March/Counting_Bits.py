# 338. Counting_Bits

def countBits(n):
	# we can use dynamic programming here
	# time comp --> O(N) space comp --> O(1)
	dp = [0]*(n+1)
	offset = 1
	for i in range(1, n+1):
		if offset*2 == i:
			offset = i
		dp[i] = 1 + dp[i - offset]

	return dp


	# time comp --> O(N^2) space comp --> O(1)
	def count(n):
		cnt = 0
		while n != 0:
			n = n % (n-1)
			cnt += 1
	return cnt

	res = []
	for i in range(0, n+1):
		temp = count(i)
		res.append(temp)

	return res

if __name__ == '__main__':
	n = 2
	res = countBits(n)
	print(res)