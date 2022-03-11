# 54. Spiral Matrix

# time comp --> O(M*N) space comp --> O(1)
def spiralOrder(matrix):
	top = 0
	left = 0
	bottom = len(matrix)
	right = len(matrix[0])
	res = []
	while top < bottom and left < right:
	    for i in range(left, right):
	        res.append(matrix[top][i])
	    top += 1
	    
	    for i in range(top, bottom):
	        res.append(matrix[i][right-1])
	    right -= 1
	    
	    if not(left < right and top < bottom): break
	    
	    for i in range(right-1, left-1, -1):
	        res.append(matrix[bottom-1][i])
	    bottom -= 1
	    
	    for i in range(bottom-1, top-1, -1):
	        res.append(matrix[i][left])
	    left += 1
	
	return res

if __name__ == '__main__':
	matrix = [[1,2,3],[4,5,6],[7,8,9]]
	res = spiralOrder(matrix)
	print(res)