class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buys = [inf]*(k+1)
        profits = [0]*(k+1)

        for p in prices:
            for i in range(1, k+1):
                buys[i] = min(buys[i], p-profits[i-1])
                profits[i] = max(profits[i], p-buys[i])
        return max(profits)