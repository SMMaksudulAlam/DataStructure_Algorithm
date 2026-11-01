class Solution:
    def checkRecord(self, n: int) -> int:

        mod = 10**9 + 7
        
        #dp = {} #it gets MLE

        dp = [[[-1, -1] for _ in range(3)] for _ in range(n)]

        def atten(ind, l_count, is_abs):
            if(ind<0):
                return 1
            
            if(dp[ind][l_count][is_abs] != -1):
                return dp[ind][l_count][is_abs]

            ans = atten(ind-1, 0, is_abs) % mod
            if(is_abs == 0):
                ans  = (ans + atten(ind-1, 0, 1)) % mod
            if(l_count < 2):
                ans = (ans + atten(ind-1, l_count+1, is_abs)) % mod
            
            dp[ind][l_count][is_abs] = ans
            return ans

        ans = atten(n-1, 0, 0)
        return ans