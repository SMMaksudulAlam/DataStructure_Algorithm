class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        ans = []
        row = len(grid)
        col = len(grid[0])
        mod = 10**9+7

        for i in range(row):
            x = [0, 0] #(from up, from left)
            r = []
            for j in range(col):
                r.append(x[:])
            ans.append(r)

        ans[0][0] = [1, 0]

        q = deque()
        q.append((0, 0))
        dir = [(1, 0), (0, 1)]

        while(q):
            q_ = deque()
            track = set()
            while(q):
                x, y = q.popleft()
                if(grid[x][y]==0):
                    total = (ans[x][y][0] + ans[x][y][1]) % mod
                    for dx, dy in dir:
                        x_ = x+dx
                        y_ = dy+y
                        if(x_<row and y_<col):
                            if(dx==1):
                                ans[x_][y_][0] = (ans[x_][y_][0]+total) % mod
                            else:
                               ans[x_][y_][1] = (ans[x_][y_][1] + total) % mod
                            if((x_, y_) not in track):
                                track.add((x_, y_))
                                q_.append((x_, y_))
                else:
                    for dx, dy in dir:
                        x_ = x+dx
                        y_ = dy+y
                        if(x_<row and y_<col):
                            if(dx==1):
                                ans[x_][y_][0] = (ans[x_][y_][0] + ans[x][y][1]) % mod
                            else:
                               ans[x_][y_][1] = (ans[x_][y_][1] + ans[x][y][0])% mod
                            if((x_, y_) not in track):
                                track.add((x_, y_))
                                q_.append((x_, y_))
                q = q_
                #print(ans, q)
        return sum(ans[-1][-1]) % mod
                
        