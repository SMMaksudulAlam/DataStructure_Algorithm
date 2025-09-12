class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        s = 0
        e = len(matrix)-1
        r = -1
        while(s<=e):
            if(s==e):
                r = s
                break
            if(s+1==e):
                if(target<matrix[e][0]):
                    r = s
                else:
                    r = e
                break

            m = (s+e)//2
            if(target>=matrix[m][0]):
                s = m
            else:
                e = m
        
        ind = bisect.bisect_left(matrix[r], target)
        if(ind<len(matrix[0]) and matrix[r][ind]==target):
            return True
        return False