# 5978. Count Words Obtained After Adding a Letter
startWords = ["ant","act","tack"]
targetWords = ["tack","act","acti"]

def wordCount(startWords: list[str], targetWords: list[str]) -> int:
    n = len(startWords)
    m = len(targetWords)
    s = set()

    for i in range(n):
        word = sorted(startWords[i])
        word = ''.join(word)
        s.add(word)
    
    ans = 0

    for i in range(n):
        temp = sorted(targetWords[i])
        temp = ''.join(temp)
        flag = False
        
        for j in range(len(temp)):
            w = temp[:j] + temp[j+1:]
            
            if w in s:
                flag = True
                break

        if flag: ans += 1
    
    return ans

res = wordCount(startWords, targetWords)
print(res)