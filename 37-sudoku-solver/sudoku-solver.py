class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = {}
        cols = {}
        grids = {}
        dots = deque()

        for r in range(len(board)):
            for c in range(len(board[0])):
                if(r not in rows):
                    rows[r] = set()
                if(c not in cols):
                    cols[c] = set()
                g = (r//3)*3 + (c//3)
                if(g not in grids):
                    grids[g] = set()
                if(board[r][c]!='.'):
                    e = board[r][c]
                    rows[r].add(e)
                    cols[c].add(e)
                    grids[g].add(e)
                else:
                    dots.append((r, c))
        #print(rows, cols, grids)

        def solve():
            if(not dots):
                return True       
            r, c = dots.popleft()
            g = (r//3)*3 + (c//3)
            for ind in range(1, 10):
                i = str(ind)
                if(i not in rows[r] and i not in cols[c] and i not in grids[g]):
                    rows[r].add(i)
                    cols[c].add(i)
                    grids[g].add(i)
                    board[r][c] = i
                    ans = solve()
                    if(ans):
                        return True
                    rows[r].remove(i)
                    cols[c].remove(i)
                    grids[g].remove(i)
                    board[r][c] = '.'  
            dots.appendleft((r, c))
            return False
        solve()
                                
