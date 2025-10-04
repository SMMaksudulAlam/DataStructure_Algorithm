import heapq as hq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = []
        track = set()

        hq.heappush(h, (grid[0][0], 0, 0))
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        ln = len(grid)

        while(h):
            t, i, j = hq.heappop(h)
            if((i, j) in track):
                continue
            
            if(i == ln-1 and j==ln-1):
                return t
            track.add((i, j))

            for dx, dy in dir:
                x = dx+i
                y = dy+j
                if(0<=x<ln and 0<=y<ln):
                    if((x, y) not in track):
                        hq.heappush(h, ((max(t, grid[x][y])), x, y))
        return -1
