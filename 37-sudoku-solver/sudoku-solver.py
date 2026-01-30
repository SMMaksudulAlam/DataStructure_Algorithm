class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ln = len(board)
        rows = {i:set() for i in range(ln)}
        cols = {i:set() for i in range(ln)}
        blocks = {i:set() for i in range(ln)}

        cells = deque()

        for i in range(ln):
            for j in range(ln):
                if(board[i][j]!='.'):
                    ch = int(board[i][j])
                    blk = (i//3)*3 + (j//3)
                    rows[i].add(ch)
                    cols[j].add(ch)
                    blocks[blk].add(ch)
                else:
                    cells.append((i, j))
        

        def solve():
            i, j = cells.popleft()
            blk = (i//3)*3 + (j//3)
            for x in range(1, 10):
                if(x not in rows[i] and x not in cols[j] and x not in blocks[blk]):
                    rows[i].add(x)
                    cols[j].add(x)
                    blocks[blk].add(x)
                    board[i][j] = str(x)
                    if(not cells):
                        return True
                    solved = solve()
                    if(solved):
                        return True
                    
                    rows[i].remove(x)
                    cols[j].remove(x)
                    blocks[blk].remove(x)
                    board[i][j] = '.'

            cells.appendleft((i, j))
            return False

        solve()