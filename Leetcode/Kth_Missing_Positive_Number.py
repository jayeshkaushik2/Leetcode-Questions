# 1539. Kth Missing Positive Number

# time comp --> O(Log(N)) space comp --> O(1)
def findKthPositive(arr, k):
	# binary search
	n = len(arr)
	l = 0
	r = n-1
	
	while l <= r:
	    m = l+(r-l)//2
	    
	    if arr[m]-m-1 < k:
	        l = m+1
	    else:
	        r = m-1
	
	return l+k

	# second way brute force solution time comp --> O(N) space comp --> O(1)
	num = 1
	cnt = 0
	while cnt < k:
		if num not in arr:
			cnt += 1
		num += 1

	return num-1




if __name__ == '__main__':
	arr = [2,3,4,7,11]
	k = 5
	res = 
	print(res)