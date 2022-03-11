# 11. Container With Most Water

# time comp --> O(N) space comp --> O(1)
def maxArea(height):
	n = len(height)
	maxArea = 0
	left = 0
	right = n-1

	while left < right:
		length = min(height[left], height[right])
		width = right - left
		area = length * width
		maxArea = max(maxArea, area)

		if height[left] > height[right]:
			right -= 1
		else:
			left += 1

	return maxArea

if __name__ == '__main__':
	height = [1,8,6,2,5,4,8,3,7]
	res = maxArea(height)
	print(res)