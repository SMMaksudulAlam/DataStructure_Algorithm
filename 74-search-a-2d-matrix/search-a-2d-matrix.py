class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def resolve_ind(n):
            ln = len(matrix[0])
            row = n//ln
            col = n%ln
            return row, col
        
        left = 0
        right = len(matrix)*len(matrix[0]) - 1

        while(left<=right):
            if(left == right):
                r, c = resolve_ind(left)
                if(matrix[r][c] == target):
                    return True
                return False

            if(left+1 == right):
                r, c = resolve_ind(left)
                if(matrix[r][c] == target):
                    return True
                
                r, c = resolve_ind(right)
                if(matrix[r][c] == target):
                    return True

                return False
            
            mid = (left+right)//2
            r, c = resolve_ind(mid)

            if(matrix[r][c] <= target):
                left = mid
            else:
                right = mid
        return False