class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        for right in range(len(prices)-1):
            if(prices[right]>prices[right+1]):
                profit += max(0, prices[right]-prices[left])
                left = right+1
        
        profit += max(0, prices[-1]-prices[left])
        return profit
            

