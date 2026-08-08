class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
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
        """

        prev = [0]*(amount+1)
        prev[0] = 1

        for c in coins:
            cur = [0]*(amount+1)
            cur[0] = 1
            for ind in range(1, amount+1):
                not_take = prev[ind]
                take = 0
                if(ind-c>=0):
                    take += cur[ind-c] #repetation
                cur[ind] = take + not_take
            prev = cur
        print(prev)
        return prev[-1]