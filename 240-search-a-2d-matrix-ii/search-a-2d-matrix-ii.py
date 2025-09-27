class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:        
        for ind in range(len(matrix)):
            if(matrix[ind][0]>target):
                return False
            i = bisect.bisect_left(matrix[ind], target)
            if(0<=i<len(matrix[0]) and matrix[ind][i]==target):
                return True
        return False