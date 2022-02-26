# 242. Valid Anagram

# time comp --> O(N+M) space comp --> O(N+M) 
def isAnagram(s, t):
	# return Counter(s) == Counter(t)

	if len(s) != len(t): return False
	
	hm = {}
	for item in s:
	    if item in hm:
	        hm[item] += 1
	    else:
	        hm[item] = 1
	
	hm2 = {}
	for item in t:
	    if item in hm2:
	        hm2[item] += 1
	    else:
	        hm2[item] = 1
	
	for item in hm:
	    if item in hm2 and hm2[item] == hm[item]:
	        continue
	    else:
	        return False
	
	return True


	# if len(s) == len(t):
	#     h1 = {}
	#     n = len(s)
	#     for i in range(0, n):
	#         temp = s[i]
	#         if temp in h1:
	#             h1[temp] += 1
	#         else:
	#             h1[temp] = 1
	    
	#     for i in range(0, n):
	        
	#         temp = t[i]
	#         if temp in h1:
	#             h1[temp] -= 1
	#         else:
	#             return False
	    
	#     for item in h1:
	#         if h1[item] > 0:
	#             return False
	#     return True
	# else:
	#     return False


if __name__ == '__main__':
	s = "jayesh"
	t = "yeahsj"
	res = isAnagram(s, t)
	print(res)