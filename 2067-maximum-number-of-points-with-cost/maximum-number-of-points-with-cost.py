class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        row = len(points)
        col = len(points[0])
        for r in range(1, row):
            l2r = [0]*col
            l2r[0] = points[r-1][0]
            for c in range(1, col):
                l2r[c] = max(l2r[c-1]-1, points[r-1][c])
            
            r2l = [0]*col
            r2l[-1] = points[r-1][-1]
            for c in range(col-2, -1, -1):
                r2l[c] = max(r2l[c+1]-1, points[r-1][c])
            
            for c in range(col):
                points[r][c] += max(l2r[c], r2l[c])
            
        return max(points[-1])