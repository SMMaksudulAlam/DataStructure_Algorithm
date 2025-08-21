class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = []
        r = len(mat)
        c = len(mat[0])

        for i in range(r):
            row = [0]*c
            ans.append(row)
        
        ans[0][0] = mat[0][0]

        for i in range(1, c):
            ans[0][i] = mat[0][i]

        for i in range(1, r):
            for j in range(c):
                if(mat[i][j]==1):
                    ans[i][j] = ans[i-1][j]+1
        
        count = 0
        for i in range(r):
            for k in range(c-1, -1, -1):
                j = k
                if(ans[i][j]==0):
                    continue
                mx = ans[i][j]
                while(j>=0 and ans[i][j]>0):
                    mx = min(mx, ans[i][j])
                    count += mx
                    j-=1
            
        return count
            
