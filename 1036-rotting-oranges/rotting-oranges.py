class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dir = [(-1, 0), (1, 0), (0, -1,), (0, 1)]

        s = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==2):
                    s.add((i, j))
        time = 0
        while(s):
            s_ = set()
            for i, j in s:
                for dx, dy in dir:
                    x = i+dx
                    y = j+dy
                    if(0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]==1):
                        grid[x][y] = 2
                        s_.add((x, y))
            s = s_
            if(s):
                time+=1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]==1):
                    return -1
        return time