class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  
        rows = []      
        for r in range(len(matrix)):
            if(matrix[r][0]>target):
                break
            if(matrix[r][0]<=target<=matrix[r][-1]):
                rows.append(r)
        
        cols = []
        for c in range(len(matrix[0])):
            if(matrix[0][c]>target):
                break
            if(matrix[0][c]<=target<=matrix[-1][c]):
                cols.append(c)
        
        for r in rows:
            for c in cols:
                if(matrix[r][c]==target):
                    return True
        return False