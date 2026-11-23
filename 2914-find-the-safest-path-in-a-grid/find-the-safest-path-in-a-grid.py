import heapq as hq
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if(grid[0][0] == 1 or grid[-1][-1] == 1):
            return 0

        row = len(grid)
        col = len(grid[0])

        closest_distance_from_thief = []
        for _ in range(row):
            temp = [math.inf]*col
            closest_distance_from_thief.append(temp)

        lst = []
        resolved_cell = set()
        for i in range(row):
            for j in range(col):
                if(grid[i][j] == 1):
                    lst.append((i, j))
                    resolved_cell.add((i, j))
                    closest_distance_from_thief[i][j] = 0
        
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def build_closest_distance_from_thief():
            nonlocal lst
            while(lst):
                lst_ = []
                while(lst):
                    i, j = lst.pop()
                    for di, dj in dir:
                        i_ = di+i
                        j_ = dj+j
                        if(0<=i_<row and 0<=j_<col and (i_, j_) not in resolved_cell):
                            resolved_cell.add((i_, j_))
                            closest_distance_from_thief[i_][j_] = closest_distance_from_thief[i][j] + 1
                            lst_.append((i_, j_))
                if(lst_):
                    lst = lst_
            return
                            
        build_closest_distance_from_thief()
        visited = set()
        h = []
        h.append((-closest_distance_from_thief[0][0], 0, 0))
        

        while(h):
            dis, i, j = hq.heappop(h)
            dis = -dis
            if(i == row-1 and j==col-1):
                return dis
            
            if((i, j) in visited):
                continue
            visited.add((i, j))

            for di, dj in dir:
                i_ = di+i
                j_ = dj+j
                if(0<=i_<row and 0<=j_<col and (i_, j_) not in visited):
                    dis_ = closest_distance_from_thief[i_][j_]
                    dis_ = min(dis, dis_)
                    hq.heappush(h, (-dis_, i_, j_))
        return 0

        #TC --> (R*C)^2