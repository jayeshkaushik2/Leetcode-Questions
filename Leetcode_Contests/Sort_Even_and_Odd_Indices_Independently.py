# 2164. Sort Even and Odd Indices Independently

# time comp --> O(Nlog(N)) space comp --> O(N)
def sortEvenOdd(nums: list[int]) -> list[int]:
	odd = []
	even = []
	n = len(nums)
	
	for i in range(n):
	    if i%2 == 0:
	        even.append(nums[i])
	    else:
	        odd.append(nums[i])
	    
	even.sort()
	odd.sort(reverse=True)
	res = [0]*n
	j = 0
	k = 0
	for i in range(n):
	    if i%2 == 0:
	        res[i] = even[j]
	        j += 1
	    else:
	        res[i] = odd[k]
	        k += 1
	
	return res

if __name__ == '__main__':
	nums = [4,1,2,3]
	res = sortEvenOdd(nums)
	print(res)