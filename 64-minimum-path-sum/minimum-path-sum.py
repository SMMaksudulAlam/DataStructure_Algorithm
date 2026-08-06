import heapq as hq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        row = len(grid)-1
        col = len(grid[0])-1

        def traverse(i, j):
            if((i, j) in dp):
                return dp[(i, j)]
            if(i==row and j==col):
                return grid[i][j]
            if(i>row or j>col):
                return inf
            
            dp[(i, j)] = grid[i][j] + min(traverse(i+1, j), traverse(i, j+1))
            return dp[(i, j)]
        
        return traverse(0, 0)
