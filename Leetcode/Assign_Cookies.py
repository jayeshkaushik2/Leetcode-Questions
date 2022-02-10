# 455. Assign Cookies

# time comp --> O(N) space comp --> O(1)
def findContentChildren(self, g, s):
    g.sort()
    s.sort()
    n = len(g)
    m = len(s)
    i = 0
    j = 0
    
    while i < n and j < m:
        if g[i] <= s[j]:
            i += 1
            j += 1
        else:
            j += 1
    
    return i


if __name__ == '__main__':
	g = [1,2,3]
	s = [1,1]
	res = 
	print(res)