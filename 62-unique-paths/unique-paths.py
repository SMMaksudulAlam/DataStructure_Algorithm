class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dir = [(1, 0), (0, 1)]
        track = set()
        ans = [[0]*n for _ in range(m)]

        track.add((0, 0))
        ans[0][0] = 1

        while(track):
            local_track = set()
            for x, y in track:
                for dx, dy in dir:
                    x_ = x+dx
                    y_ = y+dy
                    if(x_<m and y_<n):
                        ans[x_][y_] += ans[x][y]
                        local_track.add((x_, y_))
            track = local_track
        return ans[-1][-1]
            
        