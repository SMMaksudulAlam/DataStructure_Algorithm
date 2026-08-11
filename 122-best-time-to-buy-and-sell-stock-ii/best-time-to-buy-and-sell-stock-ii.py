class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        mxp = prices[0]
        mnp = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            p = prices[i]
            if(p < mxp):
                profit += (mxp-mnp)
                mnp = p
            mxp = p
        profit += (mxp-mnp)
        return profit
        """

        dp = {}
        def make_profit(ind, couldBuy):
            if((ind, couldBuy) in dp):
                return dp[(ind, couldBuy)]
            if(ind == len(prices)):
                return 0
            profit = 0
            if(couldBuy==1):
                profit = max(-prices[ind] + make_profit(ind+1, 0), make_profit(ind+1, 1))
            else:
                profit = max(prices[ind] + make_profit(ind+1, 1), make_profit(ind+1, 0))
            dp[(ind, couldBuy)] = profit
            return dp[(ind, couldBuy)]
        
        profit = make_profit(0, 1)
        return profit

