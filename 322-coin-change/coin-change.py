class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def min_coin(rem, ind):
            if((rem, ind) in dp):
                return dp[(rem, ind)]
            if(rem < 0 or ind < 0):
                return inf

            if(rem == 0):
                return 0
            
            take = 1 + min_coin(rem - coins[ind], ind)
            not_take = min_coin(rem, ind-1)

            dp[(rem, ind)] =  min(take, not_take)
            return dp[(rem, ind)]
    
        ans = min_coin(amount, len(coins)-1)
        return -1 if ans == inf else ans