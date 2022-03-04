# 122. Best Time to Buy and Sell Stock II

# time comp --> O(N) space comp --> O(1)
def maxProfit(prices):
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]
        
        return maxProfit

if __name__ == '__main__':
	prices = [7,1,5,3,6,4]
	res = maxProfit(prices)
	print(res)