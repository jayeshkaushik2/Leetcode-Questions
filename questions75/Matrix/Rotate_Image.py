# 48. Rotate Image

# time comp --> O(N*N) space comp --> O(1)
def rotate(matrix):
	n = len(matrix)
	
	for i in range(n):
	    for j in range(i+1, n):
	        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
	
	for ele in matrix:
	    ele.reverse()

if __name__ == '__main__':
	matrix = [[1,2,3],[4,5,6],[7,8,9]]
	rotate(matrix)
	print(matrix)