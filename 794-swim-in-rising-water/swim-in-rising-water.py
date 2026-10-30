import heapq as hq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        h = []
        visited = set()
        h.append((grid[0][0], 0, 0))

        ln = len(grid)

        while(h):
            cst, i, j = hq.heappop(h)
            if(i==ln-1 and j==ln-1):
                return cst
            if((i, j) in visited):
                continue
            
            visited.add((i,j))

            for di, dj in dir:
                i_ = di+i
                j_ = dj+j
                if(0<=i_<ln and 0<=j_<ln):
                    if((i_, j_) not in visited):
                        hq.heappush(h, (max(cst, grid[i_][j_]), i_, j_))
        
        return -1