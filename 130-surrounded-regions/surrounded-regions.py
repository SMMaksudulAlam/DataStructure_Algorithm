class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        visited = set()
        edge_connected = []
        
        row = len(board)
        col = len(board[0])

        for r in range(row):
            if(r==0 or r==row-1):
                for c in range(col):
                    if(board[r][c]=="O"):
                        edge_connected.append((r, c))
            else:
                if(board[r][0]=="O"):
                    edge_connected.append((r, 0))
                if(board[r][col-1]=="O"):
                    edge_connected.append((r, col-1))
        #print(edge_connected)

        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def track_edge_connected(i, j):
            visited.add((i, j))
            for (di, dj) in dir:
                i_ = i+di
                j_ = j+dj

                if((0<=i_<row and 0<=j_<col) and board[i_][j_] == "O" and ((i_, j_) not in visited)):
                    track_edge_connected(i_, j_)
            return

        for (i, j) in edge_connected:
            if((i, j) not in visited):
                track_edge_connected(i, j)

        #print(visited)


        def filler(i, j):
            board[i][j] = "X"
            for (di, dj) in dir:
                i_ = i+di
                j_ = j+dj

                if((0<=i_<row and 0<=j_<col) and board[i_][j_] == "O"):
                    filler(i_, j_)
            return

        for i in range(1, row-1):
            for j in range(1, col-1):
                if(board[i][j] == "O" and ((i, j) not in visited)):
                    filler(i, j)
        return
