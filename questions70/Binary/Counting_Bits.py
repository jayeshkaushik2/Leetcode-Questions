# 338. Counting Bits

# time comp --> O(N^2) space comp --> O(N)
def countBits(n: int) -> list[int]:
	res = [0]

	for i in range(1, n+1):
		cnt = 0
		while i != 0:
			i = i & (i-1)
			cnt += 1

		res.append(cnt)

	return res



if __name__ == '__main__':
	n = 2
	res = countBits(n)
	print(res)