class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = []
        r = len(matrix)
        c = len(matrix[0])

        count = 0

        row = []
        for i in range(c):
            x = matrix[0][i]
            row.append(x)
            if(x==1):
                count+=1
        ans.append(row)

        for i in range(1, r):
            x = matrix[i][0]
            row = [x]+[0]*(c-1)
            if(x==1):
                count+=1
            ans.append(row)

        
        for i in range(1, r):
            for j in range(1, c):
                if(matrix[i][j]==0):
                    continue
                
                ans[i][j] = min(ans[i-1][j-1], ans[i-1][j], ans[i][j-1])+1
                x = ans[i][j]
                count += x
        #print(ans)
        return count