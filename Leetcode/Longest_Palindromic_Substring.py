# 5. Longest Palindromic Substring

def longestPalindrome(s: str) -> str:
    # time comp --> O(N * N) space comp --> O(N)
    res = ""
    resLen = 0
    
    def compare(l, r, resLen, res):
        temp = ""
        tempLen = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r-l+1) > resLen:
                tempLen = r-l+1
                temp = s[l:r+1]
            l -= 1
            r += 1
            
        return temp

    for i in range(len(s)):
        temp = compare(i, i, resLen, res)
        if len(temp) > len(res):
            res = temp
            
        temp = compare(i, i+1, resLen, res)
        if len(temp) > len(res):
            res = temp
    
    return res




    # Brute force solution
    # time comp --> O(N^2) space comp --> O(1)
    if len(s) == 1 or len(s) == 0:
        return s
    
    res = s[0]
    for i in range(len(s)):
        temp = s[i]
        for j in range(i+1, len(s)):
            temp += s[j]
            if temp == temp[::-1] and len(temp) > len(res):
                res = temp
    return res

if __name__ == '__main__':
    s = "babad"
    res = longestPalindrome(s)
    print(res)