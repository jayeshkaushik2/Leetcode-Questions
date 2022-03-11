# 73. Set Matrix Zeroes

# time comp --> O(M*N) space comp --> O(1)
def setZeroes(matrix):
	m = len(matrix)
	n = len(matrix[0])
	rw = False
	
	# CHECKING which row or col has the 0
	for i in range(m):
	    for j in range(n):
	        if i > 0:
	            if matrix[i][j] == 0:
	                matrix[0][j] = 0
	                matrix[i][0] = 0
	        else:
	            if matrix[i][j] == 0:
	                rw = True
	
	for i in range(1, m):
	    for j in range(1, n):
	        if matrix[0][j] == 0 or matrix[i][0] == 0:
	            matrix[i][j] = 0
	
	if matrix[0][0] == 0:
	    for i in range(m):
	        matrix[i][0] = 0
	if rw:
	    for j in range(n):
	        matrix[0][j] = 0

if __name__ == '__main__':
	matrix = [[1,1,1],[1,0,1],[1,1,1]]
	setZeroes(matrix)
	print(matrix)