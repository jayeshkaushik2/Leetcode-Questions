# 2185. Counting Words With a Given Prefix

# time comp --> O(N) space comp --> O(1)
def prefixCount(word, pref):
	# in one line
	return sum(1 for w in words if w.startswith(pref))
	
	res = 0
	for w in word:
		if w[:len(pref)] == pref:
			res += 1

	return res

if __name__ == '__main__':
	words = ["pay","attention","practice","attend"]
	pref = "at"
	res = prefixCount(word, pref)
	print(res)