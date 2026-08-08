class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
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
        """
        
        if(amount == 0):
            return 0
        dp = [inf]*(amount+1)

        for ind in range(amount + 1):
            for c in coins:
                _ind = ind-c 
                if(_ind >= 0):
                    if(_ind == 0):
                        dp[ind] = 1
                    elif(dp[_ind] != inf):
                        dp[ind] = min(dp[ind], 1+dp[_ind])
        return dp[amount] if dp[amount] != inf else -1