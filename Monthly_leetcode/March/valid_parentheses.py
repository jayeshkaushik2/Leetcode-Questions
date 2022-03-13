# valid parentheses

# time comp --> O(N) space comp --> O(1)
def validParentheses(nums):
	n = len(nums)
	if n % 2 != 0:
		return False

	stack = []
	for i in range(n):
		br = nums[i]
		if br in ['(', '{', '[']:
			stack.append(br)
		else:
			if stack == []: return False
			if br == ')' and stack[-1] != '(':
				return False
			if br == '}' and stack[-1] != '{':
				return False
			if br == ']' and stack[-1] != '[':
				return False
			stack.pop()

	if stack != []:
		return False

	return True

if __name__ == '__main__':
	nums = ['{', '[', '(', ')', ']', '}']
	res = validParentheses(nums)
	print(res)