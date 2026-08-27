class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: 
            return 0

        b, s = 0, 1
        maxProfit = 0

        while s < len(prices):
            buy = prices[b]
            sell = prices[s]

            if buy < sell:
                # Otherwise 0; no need to update
                maxProfit = max(maxProfit, sell - buy)
            else:
                # Keeps buy @ initial or < sell at all times
                # Means buy will have the opportunity to be every sell
                b = s
            
            s += 1

        return maxProfit
        