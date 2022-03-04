# 1528. Shuffle String

def restoreString(self, s: str, indices: list[int]) -> str:        
    n = len(indices)
    ans = [0]*n
    j = 0
    for i in indices:
        ans[i] = s[j]
        j += 1
        
    ans = "".join(ans)
    
    return ans

if __name__ == '__main__':
    s = "codeleet"
    indices = [4,5,6,7,0,2,1,3]
    res = restoreString(s, indices)
    print(res)