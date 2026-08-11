import heapq as hq
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def make_profit(ind, couldBuy, tx):
            if((ind, couldBuy, tx) in dp):
                return dp[(ind, couldBuy, tx)]
            if(ind == len(prices)):
                return 0
            profit = 0
            if(couldBuy==1):
                p1 = 0
                if(tx<2):
                    p1 = -prices[ind] + make_profit(ind+1, 0, tx+1)
                    p2 = make_profit(ind+1, 1, tx)
                    profit = max(p1, p2)
            else:
                profit = max(prices[ind] + make_profit(ind+1, 1, tx), make_profit(ind+1, 0, tx))
            dp[(ind, couldBuy, tx)] = profit
            return dp[(ind, couldBuy, tx)]
        
        profit = make_profit(0, 1, 0)
        return profit