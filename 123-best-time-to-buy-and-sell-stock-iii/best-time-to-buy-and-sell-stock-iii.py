import heapq as hq
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = inf
        profit = 0
        first_profit = 0
        second_buy = inf

        for p in prices:
            buy = min(buy, p)
            first_profit = max(first_profit, p-buy)

            second_buy = min(second_buy, p-first_profit)
            profit = max(profit, p-second_buy)
        
        return profit