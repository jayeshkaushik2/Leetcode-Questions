# 378. Kth Smallest Element in a Sorted Matrix


def kthSmallest(matrix: list[list[int]], k: int) -> int:
	'''
	There are two solution for this question:
	1> Brute force solution --> time comp --> O(N^2) space comp --> O(N^2)
	2> Optimized solution --> time comp --> O(N * log(N) * log(N)) space comp --> O(1)
	'''

	# optimized solution
	'''
	check mid element from first element to the last element in matrix
	check how many elements are smaller element then mid --> count
	then compare count and k if count < k --> left = mid + 1 else right = mid - 1
	'''
	n = len(matrix)
	start = matrix[0][0]
	end = matrix[n-1][n-1]

	def Count_smallerElements(matrix, target):
		count = 0

		for i in range(n):
			left = 0
			right = n-1

			while left <= right:
				mid = left + (right-left)//2

				if matrix[i][mid] > target:
					right = mid - 1
				else:
					left = mid + 1
			count += left

		return count


	while start <= end:
		mid = (start + end)//2
		smaller_elements = Count_smallerElements(matrix, mid)
		
		if smaller_elements < k:
			start = mid + 1
		else:
			end = mid - 1

	return start


	# brute force solution
	# temp = []
	# n = len(matrix)

	# for i in range(n):
	# 	for j in range(n):
	# 		temp.append(matrix[i][j])

	# temp.sort()

	# for i in range(n*n):
	# 	if i == k-1:
	# 		return temp[i]

	# return -1



if __name__ == '__main__':
	matrix = [[1,5,9],[10,11,13],[12,13,15]]
	k = 8
	res = kthSmallest(matrix, k)
	print(res)