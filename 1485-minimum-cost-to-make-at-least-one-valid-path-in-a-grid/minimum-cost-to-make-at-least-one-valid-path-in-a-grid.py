class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        ans = []
        for i in range(r):
            row = [inf]*c
            ans.append(row)
        
        ans[0][0] = 0

        q = deque()
        q.append((0, 0))
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        while(q):
            x, y = q.popleft()
            d = grid[x][y]
            if(d==1 and y<c-1):
                if(ans[x][y+1]>ans[x][y]):
                    ans[x][y+1] = ans[x][y]
                    q.append((x, y+1))
            if(d==2 and y>0):
                if(ans[x][y-1]>ans[x][y]):
                    ans[x][y-1] = ans[x][y]
                    q.append((x, y-1))

            if(d==3 and x<r-1):
                if(ans[x+1][y]>ans[x][y]):
                    ans[x+1][y] = ans[x][y]
                    q.append((x+1, y))

            if(d==4 and x>0):
                if(ans[x-1][y]>ans[x][y]):
                    ans[x-1][y] = ans[x][y]
                    q.append((x-1, y))
            
            for dx, dy in dir:
                x_ = x+dx
                y_ = y+dy
                if(0<=x_<r and 0<=y_<c and ans[x_][y_]>ans[x][y]+1):
                    ans[x_][y_] = ans[x][y]+1
                    q.append((x_, y_))
        return ans[-1][-1]
