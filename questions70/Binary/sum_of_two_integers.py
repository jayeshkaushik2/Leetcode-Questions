# 371. Sum of Two Integers

# time comp --> O(N) [if we are given constant input range then time comp --> O(1)] space comp --> O(1)
def getSum(a: int, b: int) -> int:
	# since python does not work in 32 bits for integer, we have to use a mask of 32 bits

	# this is the 32 bit mask
	mask = 0xffffffff

	while (b & mask) > 0:
		# calculate the carry
		carry = (a & b) << 1
		# calculate the sum
		a = a ^ b
		b = carry

	return (a & mask) if b > 0 else a

if __name__ == '__main__':
	a, b = 1, 2
	res = getSum(a, b)
	print(res)


# but in java or c++ both supports the 32 bits integers so it is esay to code
# while (b != 0){
# 	int carry = (a & b) << 1;
# 	a = a ^ b;
# 	b = carry;
# }
# return a;