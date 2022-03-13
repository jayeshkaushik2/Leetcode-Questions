# 424. Longest Repeating Character Replacement

# time comp --> O(N) space comp --> O(N)
def characterReplacement(s: str, k: int) -> int:
	# most optimized way
	res = 0
	hm = {}
	l = 0
	n = len(s)
	# instead of getting the max value from the hm each time,
	# we can just take a variable for the max value
	maxf = 0
	for r in range(n):
	    hm[s[r]] = 1 + hm.get(s[r], 0)
	    maxf = max(maxf, hm[s[r]])
	    
	    while (r - l + 1) - maxf > k:
	        hm[s[l]] -= 1
	        l += 1
	    res = max(res, r-l+1)
	
	return res

	res = 0
	hm = {}
	l = 0
	n = len(s)
	for r in range(n):
	    hm[s[r]] = 1 + hm.get(s[r], 0)
	    
	    while (r - l + 1) - max(hm.values()) > k:
	        hm[s[l]] -= 1
	        l += 1
	    res = max(res, r-l+1)
	
	return res

if __name__ == '__main__':
	s = "ABAB"
	k = 2
	res = characterReplacement(s, k)
	print(res)