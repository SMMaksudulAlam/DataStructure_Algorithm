class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def min_coin(rem, ind):
            if((rem, ind) in dp):
                return dp[(rem, ind)]
            if(rem < 0 or ind < 0):
                return 0

            if(rem == 0):
                return 1
            
            take = min_coin(rem - coins[ind], ind)
            not_take = min_coin(rem, ind-1)

            dp[(rem, ind)] =  take + not_take
            return dp[(rem, ind)]
    
        ans = min_coin(amount, len(coins)-1)
        return ans