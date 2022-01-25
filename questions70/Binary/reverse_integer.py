# 7. Reverse Integer

# time comp --> O(x) space comp --> O(1)
import math
def reverse(x: int) -> int:
	res = 0

	Min = -2**31
	Max = 2**31

	while x:
		# to work with -ve numbers we are doing this
		digit = int(math.fmod(x, 10))
		x = int(x / 10)

		# These statements will check if the res is overflowed the 32 bits or not
		if res > Max//10 or (res == Max//10 and digit >= Max%10): return 0
		if res < Min//10 or (res == Min//10 and digit <= Min%10): return 0

		res = (res * 10) + digit

	return res

if __name__ == '__main__':
	x = -123
	res = reverse(x)
	print(res)