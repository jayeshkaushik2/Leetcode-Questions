# 392. Is Subsequence

def isSubsequence(s, t):
	# time comp --> O(max(n, m)) space comp --> O(1)
	i, j = 0, 0
	while i < len(s) and j < len(t):
		if s[i] == t[j]:
			i += 1
		j += 1

	return i == len(s)


	# time comp --> O(N*M) space comp --> O(1)
    j = 0
    for i in range(len(s)):
        flag = False
        while j < len(t):
            if s[i] == t[j]:
                flag = True
                break
            j += 1
            
        if not flag: return False
        # we don't want to repeat the comparision of the jth element again so we incremented it
        j += 1
    
    return True
                

if __name__ == '__main__':
	s = "abc"
	t = "ahbgdc"
	res = isSubsequence(s, t)
	print(res)