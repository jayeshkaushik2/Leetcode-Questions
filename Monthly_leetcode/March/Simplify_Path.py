# 71. Simplify Path

# time comp --> O(N) space comp --> O(N)
def simplifyPath(path: str) -> str:
	stack = []
	cur = ""
	for c in path + "/":
		if c == "/":
			if cur == '..':
				if stack: stack.pop()
			elif cur != '' or cur != '.':
				stack.append(cur)
			cur = ""
		else:
			cur += c

	return "/" + "/".join(stack)

if __name__ == '__main__':
	path = "/home/../jayesh/kaushik/"
	res = simplifyPath(path)
	print(res)