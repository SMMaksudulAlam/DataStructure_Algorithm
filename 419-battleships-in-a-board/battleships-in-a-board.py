class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        count = 0
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = "."
            for di, dj in dir:
                i_ = i+di
                j_ = j+dj
                if(0<=i_<row and 0<=j_<col and board[i_][j_]=='X'):
                    dfs(i_, j_)
            return
        
        for i in range(row):
            for j in range(col):
                if(board[i][j]=='X'):
                    count += 1
                    dfs(i, j)
        return count

