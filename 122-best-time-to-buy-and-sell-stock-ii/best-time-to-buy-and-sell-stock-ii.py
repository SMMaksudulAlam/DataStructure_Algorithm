class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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

