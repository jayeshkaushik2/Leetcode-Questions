# 2180. Count Integers With Even Digit Sum

# time comp --> O(N^2) space comp --> O(1)
def countEven(num: int) -> int:
	res = 0

	def check(n):
	    sumis = 0
	    while n:
	        digit = n%10
	        sumis += digit
	        n = n//10

	    if sumis % 2 == 0: return 1
	    else: return 0

	for i in range(2, num+1):
	    if check(i):
	        res += 1

	return res

if __name__ == '__main__':
	num = 4
	res = countEven(num)
	print(res)