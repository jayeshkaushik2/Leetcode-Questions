# 42. Trapping Rain Water

# time comp --> O(N) space comp --> (2N)
def trap(self, height):
	n = len(height)
	left = [0]*n
	right = [0]*n
	
	left[0] = height[0]
	for i in range(1, n):
	    left[i] = max(left[i-1], height[i])
	
	right[-1] = height[-1]
	for i in range(n-2, -1, -1):
	    right[i] = max(right[i+1], height[i])
	
	print(left, right)
	water = 0
	for i in range(n):
	    water += min(left[i], right[i]) - height[i]
	
	return water


if __name__ == '__main__':
	height = [0,1,0,2,1,0,1,3,2,1,2,1]
	res = 
	print(res)