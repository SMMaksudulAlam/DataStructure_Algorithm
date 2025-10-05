class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        dic = {}

        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def traverse(i, j):
            nonlocal row, col
            if (i, j) in dic:
                return dic[(i, j)]
            ans = 1
            ans_ = 0
            for dx, dy in dir:
                x = dx+i
                y = dy+j
                if(0<=x<row and 0<=y<col and matrix[x][y]>matrix[i][j]):
                    ans_ = max(ans_, traverse(x, y))
            dic[(i, j)] = ans+ans_
            return ans+ans_

        for i in range(row):
            for j in range(col):
                traverse(i, j)
        return max(dic.values())

            

        