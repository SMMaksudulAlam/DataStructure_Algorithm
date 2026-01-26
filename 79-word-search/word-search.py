class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        track = set()
        def dfs(ind, x, y):
            nonlocal word
            if(ind >= len(word)-1):
                return True
            
            track.add((x, y))

            for dx, dy in dir:
                x_ = x+dx
                y_ = y+dy
                if(0<=x_<len(board) and 0<=y_<len(board[0])):
                    if(word[ind+1] == board[x_][y_] and (x_, y_) not in track):
                        if(dfs(ind+1, x_, y_)):
                            track.remove((x, y))
                            return True
            track.remove((x, y))
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(word[0] == board[i][j]):
                    if(dfs(0, i, j)):
                        return True
        return False

            
