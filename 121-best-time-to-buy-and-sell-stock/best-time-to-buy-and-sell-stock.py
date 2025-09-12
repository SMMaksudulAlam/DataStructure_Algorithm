class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = prices[0]
        high = low

        for i in range(len(prices)):
            if(prices[i]<low):
                profit = max(profit, high-low)
                low = prices[i]
                high = low
            if(prices[i]>high):
                high = prices[i]
        profit = max(profit, high-low)
        return profit

