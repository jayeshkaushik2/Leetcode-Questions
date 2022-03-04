# Pascal's Triangle II

def getRow(rowIndex):
	# time comp --> O(N) space comp --> (1)
	row = [1]
	for r in range(1, rowIndex+1):
		# formula we are using here is --> (n/(r-1) * (n-r+1)/r)
		row.append(row[r-1] * (rowIndex-r+1)//r)

	return row


	# time comp --> O(N^2) space comp --> O(N^2)
	res = [[1]]
	
	for i in range(2, rowIndex+2):
	    temp = [0] + res[-1] + [0]
	    subset = []
	    for i in range(1, len(temp)):
	        subset.append(temp[i-1] + temp[i])
	    res.append(subset)
	
	return res[rowIndex]

if __name__ == '__main__':
	rowIndex = 5
	res = getRow(rowIndex)
	print(res)