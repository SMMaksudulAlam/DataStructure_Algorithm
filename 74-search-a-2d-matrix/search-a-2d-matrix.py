class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if(matrix[0][0]>target or matrix[-1][-1]<target):
            return False
        s = 0
        rows = len(matrix)
        cols = len(matrix[0])
        e = rows*cols

        while(s<=e):
            if(s==e):
                row = s//cols
                col = s%cols
                if(matrix[row][col]==target):
                    return True
                return False
            
            if(s+1==e):
                row = s//cols
                col = s%cols
                if(matrix[row][col]==target):
                    return True
                row = e//cols
                col = e%cols
                if(matrix[row][col]==target):
                    return True
                return False
            
            mid = (s+e)//2
            row = mid//cols
            col = mid%cols
            if(matrix[row][col]>=target):
                e = mid
            else:
                s = mid
        return False

            