class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        parts = []
        i = 1
        mod = 10**9+7
        while(i**x<=n):
            parts.append(i**x)
            i+=1
        
        ans = []
        for i in range(len(parts)+1):
            row = [0]*(n+1)
            ans.append(row)
        
        ans[0][0] = 1

        for i in range(1, len(parts)+1):
            p = parts[i-1]
            for j in range(n+1):
                ans[i][j] = ans[i-1][j]
                if(j-p>=0):
                    ans[i][j] = (ans[i][j]+ans[i-1][j-p])%mod
        
        return ans[-1][-1]