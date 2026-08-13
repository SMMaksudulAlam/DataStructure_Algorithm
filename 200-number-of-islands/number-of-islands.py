class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        row = len(grid)
        col = len(grid[0])

        def traverse_island(i, j):
            visited.add((i, j))
            for (di, dj) in dir:
                i_ = i+di
                j_ = j+dj
                if((0<=i_<row and 0<=j_<col) and grid[i_][j_]=="1" and (i_, j_) not in visited):
                    traverse_island(i_, j_)
            return
        
        ans = 0
        print("xyz")
        for i in range(row):
            for j in range(col):
                if(grid[i][j]=="1" and (i, j) not in visited):
                    ans+=1
                    traverse_island(i, j)
        return ans
