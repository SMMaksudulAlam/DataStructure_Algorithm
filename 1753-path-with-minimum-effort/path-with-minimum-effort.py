import heapq as hq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        h = []
        hq.heappush(h, (0, (0, 0)))
        ans = math.inf

        row = len(heights)
        col = len(heights[0])

        visited = set()

        while(h):
            effort, (x, y) = hq.heappop(h)
            if((x, y) in visited):
                continue
            visited.add((x, y))
            if(x == row-1 and y == col-1):
                return effort
            for (dx, dy) in dir:
                x_ = x+dx
                y_ = y+dy
                if(0<=x_<row and 0<=y_<col and ((x_, y_) not in visited)):
                    effort_ = max(effort, abs(heights[x_][y_]-heights[x][y]))
                    if(effort_<ans):
                        hq.heappush(h, (effort_, (x_, y_)))
        return ans if ans != math.inf else 0