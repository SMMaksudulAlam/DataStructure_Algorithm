class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        row = len(grid)
        col = len(grid[0])

        visited = set()
        def dfs(i, j):
            if((i, j) in visited):
                return
            visited.add((i, j))
            for di, dj in dir:
                i_ = i+di
                j_ = j+dj
                if(0<=i_<row and 0<=j_<col and grid[i_][j_] == 0):
                    dfs(i_, j_)
            return

        for r in range(row):
            if(grid[r][0] == 0 and (r, 0) not in visited):
                dfs(r, 0)
            if(grid[r][col-1] == 0 and (r, col-1) not in visited):
                dfs(r, col-1)
        
        for c in range(col):
            if(grid[0][c] == 0 and (0, c) not in visited):
                dfs(0, c)
            if(grid[row-1][c] == 0 and (row-1, c) not in visited):
                dfs(row-1, c)
        
        ans = 0
        for r in range(row):
            for c in range(col):
                if(grid[r][c] == 0 and (r, c) not in visited):
                    ans += 1
                    dfs(r, c)
        return ans

        #TC --> O(n*m)       