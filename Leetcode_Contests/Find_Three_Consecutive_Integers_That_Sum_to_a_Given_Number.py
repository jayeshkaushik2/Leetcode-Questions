# 2177. Find Three Consecutive Integers That Sum to a Given Number

# time comp --> O(1) space comp --> O(1)
def sumOfThree(num: int) -> list[int]:
	if num % 3 == 0:
	    x = num//3-1
	    return [x, x+1, x+2]
	
	return []

	# time comp --> O(N) space comp --> O(1)
	# res = []
	# n = 3
	# to = 2
	# while n < num:
	#     n += 3
	# if n == num:
	#     x = (n//3)-1
	#     res.append(x)
	#     res.append(x+1)
	#     res.append(x+2)
	# return res
	

if __name__ == '__main__':
	num = 33
	res = sumOfThree(nums)
	print(res)