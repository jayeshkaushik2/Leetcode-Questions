# 946. Validate Stack Sequences


def validateStackSequences(pushed: list[int], popped: list[int]) -> bool:
    # time comp --> O(N) space comp --> O(N)
    stack = []
    n = len(pushed)
    j = 0
    for i in range(n):
        stack.append(pushed[i])
        while j < n and stack and popped[j] == stack[-1]:
            stack.pop()
            j += 1
    
    return j >= n




# time comp --> O(N) space comp --> O(N)
    stack = []
    n = len(pushed)
    j = 0
    for i in range(n):
        if pushed[i] != popped[j]:
            stack.append(pushed[i])
        else:
            stack.append(pushed[i])
            while j < n and stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
    
    while j < n:
        if stack:
            if stack[-1] == popped[j]:
                stack.pop()
            else:
                return False
        else:
            return False
        j += 1
    
    return True if not stack else False


if __name__ == '__main__':
    pushed = [1,2,3,4,5]
    popped = [4,5,3,2,1]    
    res = validateStackSequences(pushed, popped)
    print(res)