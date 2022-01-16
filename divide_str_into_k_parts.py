# 5980. Divide a String Into Groups of Size k


# time comp --> O(N) space comp --> O(1)
def divideString(s: str, k: int, fill: str) -> list[str]:
    res = []
    i = 0
    n = len(s)

    while i < n:
        w = s[i: i+k]
        if len(w) != k:
            while len(w) < k:
                w += fill
        res.append(w)
        i += k
    
    return res


if __name__ == '__main__':
    s = 'abcdefghij'
    k = 3
    fill = 'x'
    res = divideString(s, k, fill)
    print(res)