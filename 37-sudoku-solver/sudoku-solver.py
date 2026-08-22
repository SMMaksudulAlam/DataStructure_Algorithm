class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        blocks = {x: set() for x in range(n)}
        row = {x: set() for x in range(n)}
        col = {x: set() for x in range(n)}

        blanks = deque([])
        for r in range(n):
            for c in range(n):
                if(board[r][c] == "."):
                    blanks.append((r, c))
                else:
                    num = int(board[r][c])
                    row[r].add(num)
                    col[c].add(num)

                    blck = (r//3)*3 + (c//3)
                    blocks[blck].add(num)
        
        #print(row, col, blocks, blanks)

        def solve():
            if(not blanks):
                return True
            
            (r, c) = blanks.popleft()
            for num in range(1, n+1):
                num_str = str(num)
                blck = (r//3)*3 + (c//3)
                if(num not in row[r]) and (num not in col[c]) and (num not in blocks[blck]):
                    board[r][c] = num_str
                    row[r].add(num)
                    col[c].add(num)
                    blocks[blck].add(num)

                    solved = solve()
                    if(solved):
                        return True
                    
                    row[r].remove(num)
                    col[c].remove(num)
                    blocks[blck].remove(num)
                    board[r][c] = "."
            
            blanks.appendleft((r, c))
            return False
        
        solve()
        return

