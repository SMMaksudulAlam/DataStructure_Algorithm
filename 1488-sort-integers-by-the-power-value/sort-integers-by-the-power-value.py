class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        dp = {}
        def power(x):
            if(x == 1):
                return 0
            if(x in dp):
                return dp[x]
            ans = 1
            if(x % 2 == 0):
                ans += power(x//2)
            else:
                ans += power(3*x + 1)
            dp[x] = ans
            return ans

        array = []
        for i in range(lo, hi+1):
            p = power(i)
            array.append((p, i))
        
        array.sort(key = lambda x:x[0])
        return array[k-1][1]