class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        flip = 1
        for i in range(len(mat)):
            r = i
            c = 0
            diag = []
            while(r>=0 and c<len(mat[0])):
                diag.append(mat[r][c])
                r-=1
                c+=1
            if(flip==1):
                for ind in range(len(diag)):
                    ans.append(diag[ind])
                flip*=-1
            else:
                for ind in range(len(diag)-1, -1, -1):
                    ans.append(diag[ind])
                flip*=-1

        for i in range(1, len(mat[0])):
            r = len(mat)-1
            c = i
            diag = []
            while(r>=0 and c<len(mat[0])):
                diag.append(mat[r][c])
                r-=1
                c+=1
            if(flip==1):
                for ind in range(len(diag)):
                    ans.append(diag[ind])
                flip*=-1
            else:
                for ind in range(len(diag)-1, -1, -1):
                    ans.append(diag[ind])
                flip*=-1
        
        return ans