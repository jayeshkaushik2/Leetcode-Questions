# 6021. Maximize Number of Subsequences in a String

# time comp --> O(N) space comp --> O(N)
def maximumSubsequenceCount(text: str, pattern: str) -> int:
	nt = []
	
	for c in text:
	    if c in pattern:
	        nt.append(c)
	nt = "".join(nt)

	def go(s):
	    total = 0
	    seen = 0
	    for c in s:
	        if c == pattern[0]:
	            seen += 1
	        else:
	            total += seen
	    return total

	if pattern[0] == pattern[1]:
	    x = len(nt) + 1
	    return x * (x - 1) // 2

	return max(go(nt + pattern[1]), go(pattern[0] + nt))

if __name__ == '__main__':
	text = "aabb"
	pattern = "ab"
	res = maximumSubsequenceCount(text, pattern)
	print(res)