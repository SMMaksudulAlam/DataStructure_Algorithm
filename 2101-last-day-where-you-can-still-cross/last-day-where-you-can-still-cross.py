class uf:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.parent = self
    
    def find(self):
        p = self
        while(p.parent != p):
            p = p.parent
        
        cur = self
        while(cur != p):
            temp = cur.parent
            cur.parent = p
            cur = temp
        
        return p


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        """
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
        """

        """
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def dfs(i, j, p):
            if((i, j) in nodes):
                return
            nde = uf(i, j)
            nde.parent = p
            nodes[(i, j)] = nde

            for di, dj in dir:
                i_ = di+i
                j_ = dj+j
                if(0<=i_<row and 0<=j_<col and (i_, j_) not in s):
                    dfs(i_, j_, p)
            return
            """

        s = set()
        for i in range(len(cells)):
            s.add((cells[i][0]-1, cells[i][1]-1))
        
        nodes = {}
        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def gen_and_merge(i, j):
            nde = uf(i, j)
            nodes[(i, j)] = nde

            neigh_p = [nde]
            top = None if nde.i != 0 else nde
            bottom = None if nde.i != row-1 else nde
            final_p = nde

            for di, dj in dir:
                i_ = di+i
                j_ = dj+j
                if(0<=i_<row and 0<=j_<col and (i_, j_) in nodes):
                    p = nodes[(i_, j_)].find()
                    if(p.i == 0):
                        top = p
                        final_p = p
                    if(p.i == row-1):
                        bottom = p
                        final_p = p
                    neigh_p.append(p)

            if(top != None and bottom != None):
                return True

            nde.parent = final_p
            for p in neigh_p:
                p.parent = final_p
        
            return False

        for ind in range(len(cells)-1, -1, -1):
            i, j = cells[ind]
            i-=1
            j-=1

            if(gen_and_merge(i, j) == True):
                return ind
        
        return -1