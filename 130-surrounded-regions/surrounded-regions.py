class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        dir = [(-1, 0), (1, 0), (0, -1,), (0, 1)]

        def dfs(i, j, dic):
            dic[(i, j)] = 1
            ans = True
            for dx, dy in dir:
                x = i+dx
                y = j+dy
                if(0<=x<len(board) and 0<=y<len(board[0]) and (x, y) not in dic and board[x][y]=='O'):
                    ans_ = dfs(x, y, dic)
                    ans = ans and ans_
            if(not ans):
                return False
            if(i==0 or i==len(board)-1 or j==0 or j==len(board[0])-1):
                return False
            return True
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=='O'):
                    dic = {}
                    res = dfs(i, j, dic)
                    if(res):
                        for x, y in dic.keys():
                            board[x][y] = 'X'
                    else:
                        for x, y in dic.keys():
                            board[x][y] = 'P'

        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=='P'):
                    board[i][j]='O'


        