class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if(obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1):
            return 0
        
        obstacles = {}
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if(obstacleGrid[i][j]==1):
                    obstacles[(i, j)] = 1
        
        obstacleGrid[0][0] = 1
        s = set()
        s.add((0, 0))
        dir = [(1, 0), (0, 1)]
        while(s):
            next_s = set()
            for (x, y) in s:
                for dx, dy in dir:
                    next_x = x+dx
                    next_y = y+dy
                    if(0<=next_x<len(obstacleGrid) and 0<=next_y<len(obstacleGrid[0]) and (next_x, next_y) not in obstacles):
                        obstacleGrid[next_x][next_y] += obstacleGrid[x][y]
                        next_s.add((next_x, next_y))
            s = next_s
        return obstacleGrid[-1][-1]

        


        
