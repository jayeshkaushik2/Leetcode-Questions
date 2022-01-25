# 5991. Rearrange Array Elements by Sign


# time comp --> O(N) space comp --> O(N)
def rearrangeArray(nums: list[int]) -> list[int]:
	N = len(nums)
	p = []
	n = []

	for i in range(N):
		if nums[i] > 0:
			p.append(nums[i])
		else:
			n.append(nums[i])

	j, k = 0, 0
	for i in range(N):
		if i%2 == 0:
			nums[i] = p[j]
			j += 1
		else:
			nums[i] = n[k]
			k += 1

	return nums


if __name__ == '__main__':
	nums = [3,1,-2,-5,2,-4]
	res = rearrangeArray(nums)
	print(nums)
