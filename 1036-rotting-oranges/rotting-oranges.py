class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir = [(-1, 0), (1, 0), (0, -1,), (0, 1)]
        rotten = []
        row = len(grid)
        col = len(grid[0])
        visited = set()

        for r in range(row):
            for c in range(col):
                if(grid[r][c] == 2):
                    rotten.append((r, c))
                    visited.add((r, c))
            
        time = 0
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while(rotten):
            rotten_ = []
            while(rotten):
                (r, c) = rotten.pop()
                for (dr, dc) in dir:
                    r_ = dr + r
                    c_ = dc + c
                    if(0<=r_<row and 0<=c_<col and ((r_, c_) not in visited) and grid[r_][c_]==1):
                        rotten_.append((r_, c_))
                        visited.add((r_, c_))
                
            rotten = rotten_
            if(rotten_):
                time+=1
        
        for r in range(row):
            for c in range(col):
                if(grid[r][c] == 1 and ((r, c) not in visited)):
                    return -1
        return time