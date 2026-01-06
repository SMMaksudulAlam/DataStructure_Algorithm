class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        i = 0
        j = 0
        
        while(True):
            left = mat[i][j-1] if(j>0) else -1
            right = mat[i][j+1] if(j+1<len(mat[0])) else -1

            up = mat[i-1][j] if(i>0) else -1
            down = mat[i+1][j] if(i+1<len(mat)) else -1

            val = mat[i][j]
            if(val>left and val>right and val>up and val>down):
                return [i, j]

            if(right>left and right>val):
                j+=1
            elif(left>right and left>val):
                j-=1
            else:
                pass
            
            up = mat[i-1][j] if(i>0) else -1
            down = mat[i+1][j] if(i+1<len(mat)) else -1
            val = mat[i][j]
            if(down>up and down>val):
                i+=1
            elif(up>down and up>val):
                i-=1
            else:
                pass
        return -1


        