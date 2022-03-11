# 57. Insert Interval

def insert(intervals, newInterval):
	# time comp --> O(N) space comp --> O(1)
	n = len(intervals)
	res = []

	for i in range(n):
		if newInterval[0] < intervals[i][1]:
			res.append(newInterval)
			return res + intervals[i:]
		elif newInterval[1] > intervals[i][1]:
			res.append(intervals[i])
		else:
			first = min(intervals[i][0], newInterval[0])
			second = max(intervals[i][1], newInterval[1])
			newInterval = [first, second]

	res.append(newInterval)
	return res




	# time comp --> O(Nlog(N)) space comp --> O(1)
	intervals.append(newInterval)
	n = len(intervals)
	intervals.sort()
	
	prev = intervals[0]
	res = []
	for temp in intervals[1:]:
	    if prev[1] < temp[0]:
	        res.append(prev)
	        prev = temp
	    else:
	        if prev[1] > temp[1]:
	            prev = prev
	        else:
	            prev = [prev[0], temp[1]]
	
	res.append(prev)
	
	return res


if __name__ == '__main__':
	intervals = [[1,3],[6,9]
	newInterval = [2,5]
	res = insert(intervals, newInterval)
	print(res)