class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        row = set()
        pos_diag = set() #bottom_left to top_right --> r+c
        neg_diag = set() #bottom_right to top_left --> r-c
        points = set()

        ans = []
        def build(r):
            #print(r, row, col, pos_diag, neg_diag, points)
            if(r == n):
                ans_ar = [["."]*n for _ in range(n)]
                for (r, c) in points:
                    ans_ar[r][c] = "Q"
                ans_str = []
                for rw in ans_ar:
                    rw = "".join(rw)
                    ans_str.append(rw)
                ans.append(ans_str)
                return
            
            for c in range(n):
                if(r not in row) and (c not in col) and (r+c not in pos_diag) and (r-c not in neg_diag):
                    row.add(r)
                    col.add(c)
                    pos_diag.add(r+c)
                    neg_diag.add(r-c)
                    points.add((r, c))

                    build(r+1)

                    row.remove(r)
                    col.remove(c)
                    pos_diag.remove(r+c)
                    neg_diag.remove(r-c)
                    points.remove((r, c))
            return
        
        build(0)
        #print(ans)
        return ans






