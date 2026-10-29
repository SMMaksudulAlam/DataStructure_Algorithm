import heapq as hq
class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        #dijkstra
        #state --> (i, j, block_count)

        h = []
        visited = set()
        if(grid[0][0]==1):
            if(k==0):
                return -1
            h.append((0, 0, 0, 1))
        else:
            h.append((0, 0, 0, 0))
        
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        row = len(grid)
        col = len(grid[0])

        while(h):
            cost, i, j, blck = hq.heappop(h)
            if(i==row-1 and j==col-1):
                return cost
            
            if((i, j, blck) in visited):
                continue
            
            visited.add((i, j, blck))

            for di, dj in dir:
                i_ = i+di
                j_ = j+dj

                if(0<=i_<row and 0<=j_<col):
                    if(grid[i_][j_] == 1):
                        if(blck<k):
                            if((i_, j_, blck+1) not in visited):
                                hq.heappush(h, (cost+1, i_, j_, blck+1))
                        else:
                            continue
                    else:
                        if((i_, j_, blck) not in visited):
                                hq.heappush(h, (cost+1, i_, j_, blck))
        return -1


