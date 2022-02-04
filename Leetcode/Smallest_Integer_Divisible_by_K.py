# 1015. Smallest Integer Divisible by K

# time comp --> O(N) sapce comp --> O(1)
def smallestRepunitDivByK(k: int) -> int:
	'''
	We are using previous remainder technique
	formula to find the previous remainder is --> (prev_rem*10 + 1) % k
	'''
	if k%2 == 0 and k%5 == 0: return -1
	
	prev_remainder = 0
	
	for n in range(1, k+1):
	    prev_remainder = (prev_remainder*10 + 1) % k
	    
	    if prev_remainder == 0:
	        return n
	
	return -1

if __name__ == '__main__':
	k = 1
	res = smallestRepunitDivByK(k)
	print(res)