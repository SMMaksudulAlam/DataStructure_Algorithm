class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = 0
        tempProfit = 0
        for high in range(1, len(prices)):
            if(prices[high]<prices[low]):
                profit = max(profit, tempProfit)
                tempProfit = 0
                low = high
            else:
                tempProfit = max(tempProfit, prices[high]-prices[low])
        profit = max(profit, tempProfit)
        return profit
