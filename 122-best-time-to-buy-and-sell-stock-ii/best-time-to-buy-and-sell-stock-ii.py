class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = inf
        for p in prices:
            buy = min(buy, p-profit)
            profit = max(profit, p-buy)
        return profit
            

