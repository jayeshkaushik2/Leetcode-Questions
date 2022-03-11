# 20. Valid Parentheses

# time comp --> O(N) space comp --> O(N)
def isValid(s):
	if len(s)%2 != 0: return False
	
	stack = []
	n = len(s)
	
	for i in range(n):
	    if s[i] == "(" or s[i] == "{" or s[i] == "[":
	        stack.append(s[i])
	    else:
	        if stack == []: return False
	        if s[i] == ")" and stack[-1] != "(": return False
	        if s[i] == "}" and stack[-1] != "{": return False
	        if s[i] == "]" and stack[-1] != "[": return False
	        
	        '''
	        If the above conditions are not true mean there exists a pair of brackets
	        so, remove the last element from the stack
	        '''
	        stack.pop()
	
	if stack != []: return False
	
	return True

if __name__ == '__main__':
	s = "()"
	res = isValid(s)
	print(res)