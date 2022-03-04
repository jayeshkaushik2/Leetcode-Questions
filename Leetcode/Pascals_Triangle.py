# 118. Pascal's Triangle

# time comp --> O(N^2) space comp --> O(N^2)
def generate(numRows):
	res = [[1]]

	for i in range(2, numRows+1):
	    temp = [0] + res[-1] + [0]
	    subset = []
	    for j in range(1, len(temp)):
	        subset.append(temp[j-1] + temp[j])
	    res.append(subset)

	return res


if __name__ == '__main__':
	numRows = 5
	res = generate(numRows)
	print(res)