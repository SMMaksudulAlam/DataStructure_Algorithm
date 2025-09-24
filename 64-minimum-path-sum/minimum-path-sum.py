import heapq as hq
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        visited = set()
        h = []
        hq.heappush(h, (grid[0][0], 0, 0))
        visited.add((0, 0))

        dir = [(1, 0), (0, 1)]
        while(h):
            v, x, y = hq.heappop(h)
            for dx, dy in dir:
                x_ = x+dx
                y_ = y+dy
                if(0<=x_<len(grid) and 0<=y_<len(grid[0]) and (x_, y_) not in visited):
                    v_ = v + grid[x_][y_]
                    grid[x_][y_] = v_
                    visited.add((x_, y_))
                    hq.heappush(h, (v_, x_, y_))
        return grid[-1][-1]