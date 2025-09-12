class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = {}
        row = {}
        block = {}
        ln = len(board)

        for i in range(ln):
            for j in range(ln):
                if(board[i][j]!='.'):
                    e = board[i][j]
                    if(i not in row):
                        row[i] = {}
                    if(j not in col):
                        col[j] = {}

                    blck = (i//3)*3+(j//3)
                    if(blck not in block):
                        block[blck] = {}
                    
                    row[i][e] = row[i].get(e, 0)+1
                    col[j][e] = col[j].get(e, 0)+1
                    block[blck][e] = block[blck].get(e, 0)+1
                
        
        for d in row.values():
            if(max(d.values())>1):
                return False

        for d in col.values():
            if(max(d.values())>1):
                return False

        for d in block.values():
            if(max(d.values())>1):
                return False

        return True
                    