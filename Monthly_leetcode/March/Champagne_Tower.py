# 799. Champagne Tower

# time comp --> O(N^2) space comp --> O(N^2)
def champagneTower(poured: int, query_row: int, query_glass: int) -> float:
	# making a piramid array like 1, 11, 111, 1111...
	dp = [[0 for _ in range(x)] for x in range(1, query_row+2)]
	# lets assume we have poured all the wine on the first glass
	dp[0][0] = poured
	
	for i in range(query_row):
	    for j in range(len(dp[i])):
	    	# taking the overflow value from a perticular glass
	        overflow = (dp[i][j]-1) / 2.0
	        if overflow > 0:
	            dp[i+1][j] += overflow
	            dp[i+1][j+1] += overflow
	

	return dp[query_row][query_glass] if dp[query_row][query_glass] <= 1 else 1

if __name__ == '__main__':
	poured = 1
	query_row = 1
	query_glass = 1
	res = champagneTower(poured, query_row, query_glass)
	print(res)