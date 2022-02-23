# 3. Longest Substring Without Repeating Characters

 def lengthOfLongestSubstring(s: str) -> int:
	# this is the sliding window problem
	# time comp --> O(N) space comp --> O(N)
	charSet = set()
	l = 0
	res = 0
	
	for i in range(len(s)):
	    while s[i] in charSet:
	        charSet.remove(s[l])
	        l += 1
	    charSet.add(s[i])
	    res = max(res, i-l+1)
	
	return res
	        
	
	# brute force solution
	# time comp --> O(N^2) space comp --> O(N)
	n = len(s)
	st = []
	res = 0
	
	for i in range(n):
	    st.append(s[i])
	    j = i+1
	    while j < n and s[j] not in st:
	        st.append(s[j])
	        j += 1
	    print(res, st)
	    res = max(res, len(st))
	    st = []
	return res


if __name__ == '__main__':
	s = "abcabcbb"
	res = lengthOfLongestSubstring(s)
	print(res)