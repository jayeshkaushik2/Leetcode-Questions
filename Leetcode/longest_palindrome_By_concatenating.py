# 5962. Longest Palindrome by Concatenating Two Letter Words

from collections import Counter

words = ["lc","cl","gg"]

def longestPalindrome(words: list[str]) -> int:
    ans   = 0
    found = 0
    hm    = Counter(words)

    for item in hm:
        if item == item[::-1]:
            if hm[item] % 2 == 1:
                found = 2
            ans += (hm[item]//2 * 2) * 2
        else:
            ans += min(hm[item], hm[item[::-1]]) * 2
    
    return ans + found

    


res = longestPalindrome(words)
print(res)