import heapq as hq
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, buy2 = inf, inf
        prf = 0

        for p in prices:
            buy = min(buy, p)
            prf = max(prf, p-buy)

            buy2 = min(buy2, p-prf)
            
            profit = max(profit, p-buy2)
        return profit
