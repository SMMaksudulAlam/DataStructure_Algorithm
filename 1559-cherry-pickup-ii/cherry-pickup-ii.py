class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        dp = {}
        row = len(grid)-1
        col = len(grid[0])-1

        dir = [-1, 0, 1]

        def collect(rw, cl1, cl2):
            if((rw, cl1, cl2) in dp):
                return dp[(rw, cl1, cl2)]
            res = 0
            if(cl1 == cl2):
                res = grid[rw][cl1]
            else:
                res = grid[rw][cl1] + grid[rw][cl2]

            if(rw == row):
                dp[(rw, cl1, cl2)] = res
                return res
            else:
                mx = -inf
                for dx1 in dir:
                    if(0 <= cl1+dx1 <= col):
                        for dx2 in dir:
                            if(0 <= cl2+dx2 <= col):
                                mx = max(mx, collect(rw+1, cl1+dx1, cl2+dx2))

                dp[(rw, cl1, cl2)] = res + mx
                return res + mx
            
        return collect(0, 0, col)