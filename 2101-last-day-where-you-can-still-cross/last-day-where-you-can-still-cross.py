class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        def can_pass(mid):
            visited = set()
            for i in range(mid+1):
                visited.add((cells[i][0]-1, cells[i][1]-1))
            
            dq = []
            for i in range(col):
                if((0, i) not in visited):
                    dq.append((0, i))
                visited.add((0, i))
            
            dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            while(dq):
                dq_ = []
                while(dq):
                    i, j = dq.pop()
                    for di, dj in dir:
                        i_ = i+di
                        j_ = j+dj
                        if(0<=i_<row and 0<=j_<col):
                            if((i_, j_) not in visited):
                                if(i_ == row-1):
                                    return True
                                visited.add((i_, j_))
                                dq_.append((i_, j_))
                dq = dq_
            return False

        left = 0
        right = len(cells)-1

        last_pass = right
        while(left <= right):
            mid = (left + right) // 2
            if(can_pass(mid) == True):
                last_pass = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return last_pass + 1