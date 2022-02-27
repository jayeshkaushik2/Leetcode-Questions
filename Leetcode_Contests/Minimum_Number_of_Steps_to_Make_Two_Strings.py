# 6009. Minimum Number of Steps to Make Two Strings Anagram II


# time comp --> O(M+N) space comp --> O(26+26)
def minSteps(s: str, t: str) -> int:
	count1 = [0]*26
	for c in s:
	    count1[ord(c) - ord('a')] += 1
	
	count2 = [0]*26
	for c in t:
	    count2[ord(c) - ord('a')] += 1
	    
	res = 0
	
	for i in range(26):
	    res += abs(count1[i] - count2[i])
	
	return res

if __name__ == '__main__':
	s = "leetcode"
	t = "coats"
	res = minSteps(s, t)
	print(res)