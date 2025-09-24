import heapq as hq
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy1, buy2 = inf, inf
        prof1, prof = 0, 0

        for p in prices:
            buy1 = min(buy1, p)
            prof1 = max(prof1, p-buy1)

            buy2 = min(buy2, p-prof1)

            prof = max(prof, p-buy2)

        return prof
