# 3. Longest Substring Without Repeating Characters

# all three solutions work
 def lengthOfLongestSubstring(s: str) -> int:
	# this is the sliding window problem
	# time comp --> O(N) space comp --> O(N)
	res = 0
	charset = set()
	n = len(s)
	l = 0
	for r in range(n):
	    while s[r] in charset:
	        charset.remove(s[l])
	        l += 1
	    charset.add(s[r])
	    res = max(res, r-l+1)
	
	return res       
	
	
	
	# time comp --> O(N^2) space comp --> O(N)
	n = len(s)
	if n == 0: return 0
	
	res = 0
	cur = ""
	for i in range(0, n):
	    while s[i] in cur:
	        cur = cur[1:]
	    cur += s[i]
	    res = max(len(cur), res)
	
	return res
	
    
	# brute force solution time comp --> O(N^2) space comp --> O(N)
	res = 0
	for i in range(len(s)):
	    temp = s[i]
	    for j in range(i+1, len(s)):
	        if s[j] not in temp:
	            temp += s[j]
	        else:
	            break
	    res = max(len(temp), res)
	return res


if __name__ == '__main__':
	s = "abcabcbb"
	res = lengthOfLongestSubstring(s)
	print(res)