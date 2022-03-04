# 121. Best Time to Buy and Sell Stock

# time comp --> O(N) space comp --> O(1)
def maxProfit(prices):
	if prices == []: return 0
	
	# to keep track of the minimum price in prices
	lastMin = prices[0]
	maxProfit = 0
	# starting from the second index
	for pr in prices[1:]:
	    if pr < lastMin:
	        lastMin = pr
	    
	    profit = pr - lastMin
	    maxProfit = max(maxProfit, profit)
	
	return maxProfit

if __name__ == '__main__':
	prices = [1,2,2,6,7,8,10]
	res = maxProfit(prices)
	print(res)