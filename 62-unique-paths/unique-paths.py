class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = []
        ans.append([1]*n)
        for i in range(m-1):
            r = [0]*n
            r[0] = 1
            ans.append(r)
        for i in range(1, m):
            for j in range(1, n):
                ans[i][j] = ans[i-1][j]+ans[i][j-1]
        return ans[-1][-1]
            
        