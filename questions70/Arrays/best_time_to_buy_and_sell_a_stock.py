# 121. Best Time to Buy and Sell Stock

# time comp --> O(N) space comp --> O(1)
def maxProfit(prices):
	n = len(prices)
	lastMin = prices[0]
	ans = 0

	for i in range(n):
		if prices[i] < lastMin:
			lastMin = prices[i]

		profit = prices[i] - lastMin
		ans = max(profit, ans)

	return ans


if __name__ == '__main__':
	prices = [7,1,5,3,6,4]
	ans = maxProfit(prices)
	print(ans)