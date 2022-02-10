# 463. Island Perimeter

# Time comp --> O(N*M) space comp --> O(N*M)
def islandPerimeter(self, grid):
	# DFS or BFS both can work here
	hs = set()
	def dfs(i, j):
	    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0:
	        return 1
	    
	    if (i, j) in hs:
	        return 0
	    
	    hs.add((i, j))
	    perimeter = dfs(i, j+1)
	    perimeter += dfs(i+1, j)
	    perimeter += dfs(i, j-1)
	    perimeter += dfs(i-1, j)
	    
	    return perimeter
	
	for i in range(len(grid)):
	    for j in range(len(grid[0])):
	        if grid[i][j] == 1:
	            return dfs(i, j)

if __name__ == '__main__':
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    res = islandPerimeter(grid)
    print(grid)        