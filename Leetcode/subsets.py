# 78. Subsets
'''
time comp --> O()
'''
def SubsetArray(arr, n) -> list:
    res = []
    subset = []

    def dfs(i):
        if i >= n:
            res.append(subset.copy())
            return

        # including the element
        subset.append(arr[i])
        dfs(i + 1)
        # not including the element
        subset.pop()
        dfs(i + 1)

    dfs(0)

    return res

if __name__ == "__main__":
    arr = [1, 2, 3]
    n = len(arr)
    ans = SubsetArray(arr, n)
    print(ans)