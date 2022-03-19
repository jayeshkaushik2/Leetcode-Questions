# 1249. Minimum Remove to Make Valid Parentheses

# time comp --> O(N) space comp --> O(N)
def minRemoveToMakeValid(self, s: str) -> str:
	arr = list(s)
	res = ""
	stack = []
	n = len(arr)
	for i in range(n):
	    if arr[i] == "(":
	        stack.append(i)
	    elif arr[i] == ")":
	        if stack == []:
	            arr[i] = '.'
	        else:
	            stack.pop()
	
	for idx in stack:
	    arr[idx] = '.'
	
	for c in arr:
	    if c != '.':
	        res += c
	
	return res


if __name__ == '__main__':
	s = ""
	res = 
	print(s)