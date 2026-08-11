class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def make_profit(ind, couldBuy):
            if((ind, couldBuy) in dp):
                return dp[(ind, couldBuy)]
            if(ind >= len(prices)):
                return 0
            profit = 0
            if(couldBuy==1):
                profit = max(-prices[ind] + make_profit(ind+1, 0), make_profit(ind+1, 1))
            else:
                profit = max(prices[ind] + make_profit(ind+2, 1), make_profit(ind+1, 0))
            dp[(ind, couldBuy)] = profit
            return dp[(ind, couldBuy)]
        
        profit = make_profit(0, 1)
        return profit