# 56. Merge Intervals

# time comp --> O(log(N)) + O(N) space comp --> O(N)
def merge(intervals):
	res = []
	n = len(intervals)
	# we have to sort this array according to the first element of the elements in array
	intervals.sort(key=lambda x:x[0])
	prev = intervals[0]
	
	for i in range(1, n):
	    temp = intervals[i]
	    
	    if prev[1] < temp[0]:
	        res.append(prev)
	        prev = temp
	    elif prev[1] >= temp[0]:
	        if prev[1] > temp[1]:
	            prev = prev
	        else:
	            prev = [prev[0], temp[1]]
	
	res.append(prev)
	
	return res


if __name__ == '__main__':
	intervals = [[1,3],[2,6],[8,10],[15,18]]
	res = merge(intervals)
	print(res)