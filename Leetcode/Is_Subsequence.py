# 392. Is Subsequence

def isSubsequence(s: str, t: str) -> bool:
	# time comp --> O(N) where N = len(s) + len(t) space comp --> O(1)
	i, j = 0, 0	
	while i < len(s) and j < len(t):
	    if s[i] == t[j]:
	        i += 1
	    j += 1
	
	return i == len(s)
	
	# second solution
	# i = 0
	# for ch in s:
	#     flag = False
	#     while i < len(t):
	#         if t[i] == ch:
	#             flag = True
	#         if flag:
	#             i += 1
	#             break
	#         i += 1
	        
	#     if not flag:
	#         return False
	
	# return True

if __name__ == '__main__':
	s = "abc"
	t = "arebnmc"
	res = isSubsequence(s, t)
	print(res)