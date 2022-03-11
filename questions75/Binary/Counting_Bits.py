# 338. Counting Bits

def countBits(n: int) -> list[int]:
	# time comp --> O(N) space comp --> O(N)
	dp = [0]*(n+1)
	offset = 1

	for i in range(1, n+1):
		if offset*2 == i:
			offset = i
		dp[i] = 1 + dp[i - offset]

	return dp


	# time comp --> O(N^2) space comp --> O(N)
	# res = [0]

	# for i in range(1, n+1):
	# 	cnt = 0
	# 	while i != 0:
	# 		i = i & (i-1)
	# 		cnt += 1

	# 	res.append(cnt)

	# return res



if __name__ == '__main__':
	n = 2
	res = countBits(n)
	print(res)