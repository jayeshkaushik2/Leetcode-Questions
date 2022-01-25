# 5971. Minimum Cost of Buying Candies With Discount

# time comp --> O(N) space comp --> O(1)
def minimumCost(cost: list[int]) -> int:
	n = len(cost)
	cost.sort(reverse=True)
	ans = 0
	i = 0

	while i < n-1:
		candy1 = cost[i]
		candy2 = cost[i+1]
		ans += candy2 + candy1
		val = min(candy2, candy1)

		if i+1 < n and cost[i+1] <= val:
			i += 1

		i += 2

	while i < n:
		ans += cost[i]
		i += 1

	return ans




if __name__ == '__main__':
	cost = [6,5,7,9,2,2]
	res = minimumCost(cost)
	print(res)