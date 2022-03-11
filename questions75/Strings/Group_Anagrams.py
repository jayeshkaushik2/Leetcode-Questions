# 49. Group Anagrams

def groupAnagrams(strs):
	# time comp --> O(N) space comp --> O(N)
	res = defaultdict(list)

	for s in strs:
		count = [0]*26

		for c in s:
			count[ord(c) - ord('a')] += 1
		res[count].append(s)

	return res.values()


	# time comp --> O(N^2) space comp --> O(N)
	res = []
	n = len(strs)
	check = [1]*n
	
	for i in range(n):
	    if check[i]:
	        temp = []
	        hm1  = Counter(strs[i])
	        temp.append(strs[i])
	        check[i] = 0
	        
	        for j in range(i+1, n):
	            hm2 = Counter(strs[j])
	            if check[j] and hm1 == hm2:
	                temp.append(strs[j])
	                check[j] = 0
	                
	        res.append(temp)
	
	return res

if __name__ == '__main__':
	strs = ["eat","tea","tan","ate","nat","bat"]
	res = 
	print(res)