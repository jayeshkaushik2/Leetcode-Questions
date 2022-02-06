# 6001. Smallest Value of the Rearranged Number

# time comp --> O(Nlog(N)) space comp --> O(N)
def smallestNumber(num):
	if num == 0:
	    return 0
	
	if num < 0:
	    n = 0-num
	    n = list(str(n))
	    n.sort(reverse=True)
	    num = 0-int("".join(n))
	    return num
	else:
	    n = num
	    n = list(str(n))
	    n.sort()
	    
	    if n[0] == "0":
	        i = 0
	        while i < len(n) and n[i] == "0":
	            i += 1
	        n[i],n[0] = n[0],n[i]
	    
	    num = int("".join(n))
	    return num


if __name__ == '__main__':
	num = 310
	res = smallestNumber(num)
	print(res)