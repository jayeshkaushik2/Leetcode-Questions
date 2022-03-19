# 856. Score of Parentheses

# time comp --> O(N) space comp --> O(N)
def scoreOfParentheses(s: str) -> int:
    n = len(s)
    stack = []
    for i in range(n):
        if s[i] == '(': stack.append(0)
        else:
            val = 0
            while stack[-1] != 0: val += stack.pop()
            val = max(val*2, 1)
            stack.pop()
            stack.append(val)
    
    score = 0
    for val in stack:
        score += val
    
    return score

if __name__ == '__main__':
    s = "(()())()(())"
    res = scoreOfParentheses(s)
    print(res)