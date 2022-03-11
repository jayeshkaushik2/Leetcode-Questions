# 79. Word Search

# time comp --> O(N*M* 4^len(word)) space comp --> O(1)
def exist(board, word):
    # USING backtracking
    rows = len(board)
    cols = len(board[0])
    path = set()
    
    def dfs(r, c, i):
        if i == len(word): return True
        if (r < 0 or c < 0 or
            r >= rows or c >= cols or
            board[r][c] != word[i] or
            (r, c) in path):
            return False
        
        path.add((r,c))
        res = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1)or
               dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
        
        path.remove((r,c))
        return res

    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0): return True
    
    return False

if __name__ == '__main__':
	board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
	word = "ABCCED"
	res = exist(board, word)
	print(res)