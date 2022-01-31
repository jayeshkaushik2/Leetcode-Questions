# 435. Non-overlapping Intervals

# time comp --> O(Nlog(N)) space comp --> O(N)
def eraseOverlapIntervals(intervals):
	'''
	sort the array
	find prevEnd with each itration
	check if they are over lapping or not
	if yes increment cnt and prevEnd = min(prevEnd, end)
	else prevEnd = end
	'''
	n = len(intervals)
	intervals.sort()
	prevEnd = intervals[0][1]
	res = 0

	for start, end in intervals[1:]:
		if start >= prevEnd:
			prevEnd = end
		else:
			res += 1
			prevEnd = min(prevEnd, end)

	return res


if __name__ == '__main__':
	intervals = [[1,2],[2,3],[3,4],[1,3]]
	res = eraseOverlapIntervals(intervals)
	print(res)