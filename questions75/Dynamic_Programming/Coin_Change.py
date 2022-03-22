# 322. Coin Change

# time comp --> O((amount + 1) * len(coins)) space comp --> O(amount + 1)
def coinChange(coins: list[int], amount: int) -> int:
	dp = [amount + 1] * (amount+1)
	dp[0] = 0
	
	for i in range(1, amount+1):
	    for c in coins:
	        if i - c >= 0:
	            dp[i] = min(dp[i], 1 + dp[i-c])
	
	return dp[amount] if dp[amount] != amount+1 else -1

if __name__ == '__main__':
	coins = [1,2,5]
	amount = 11
	res = coinChange(coins, amount)
	print(res)