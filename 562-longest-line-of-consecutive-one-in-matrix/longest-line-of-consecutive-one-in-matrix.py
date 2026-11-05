class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        ans = 0
        def row(r):
            nonlocal ans
            count = 0
            for c in range(len(mat[0])):
                if(mat[r][c]==0):
                    count = 0
                else:
                    count += 1
                    ans = max(ans, count)
            return
        
        def col(c):
            nonlocal ans
            count = 0
            for r in range(len(mat)):
                if(mat[r][c]==0):
                    count = 0
                else:
                    count += 1
                    ans = max(ans, count)
            return

        def diag(i, j): #/
            nonlocal ans
            r = len(mat)
            c = len(mat[0])
            count = 0
            while(0<=i<r and 0<=j<c):
                if(mat[i][j]==0):
                    count = 0
                else:
                    count += 1
                    ans = max(ans, count)
                i-=1
                j+=1
            return
        
        def anti_diag(i, j): #\
            nonlocal ans
            r = len(mat)
            c = len(mat[0])
            count = 0
            while(0<=i<r and 0<=j<c):
                if(mat[i][j]==0):
                    count = 0
                else:
                    count += 1
                    ans = max(ans, count)
                i+=1
                j+=1
            return
        
        for r in range(len(mat)):
            row(r)
            diag(r, 0)
            anti_diag(r, 0)

        for c in range(len(mat[0])):
            col(c)
            diag(len(mat)-1, c)
            anti_diag(0, c)

        return ans
