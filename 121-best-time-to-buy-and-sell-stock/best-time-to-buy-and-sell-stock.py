class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for e in prices:
            buy = min(buy, e)
            profit = max(profit, e - buy)
        return profit

