# 191. Number of 1 Bits

# time comp --> O(N) space comp --> O(1)
def hammingWeight(n: int) -> int:
	cnt = 0
	while n != 0:
		if n & 1: cnt += 1
		n = n << 1

	return cnt


if __name__ == '__main__':
	n = 11
	res = hammingWeight(n)
	print(res)