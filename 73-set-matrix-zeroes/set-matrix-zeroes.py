class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        def make_column_z(c):
            for r in range(len(matrix)):
                if(matrix[r][c]!=0):
                    matrix[r][c] = 'z'
            return
        
        def make_row_z(r):
            for c in range(len(matrix[0])):
                if(matrix[r][c]!=0):
                    matrix[r][c] = 'z'
            return
        
        for r in range(len(matrix)):
            isZ = False
            for c in range(len(matrix[0])):
                if(matrix[r][c]==0):
                    make_column_z(c)
                    isZ = True
            if(isZ):
                make_row_z(r)
        
        #print(matrix)
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if(matrix[r][c]=='z'):
                    matrix[r][c]=0

        return