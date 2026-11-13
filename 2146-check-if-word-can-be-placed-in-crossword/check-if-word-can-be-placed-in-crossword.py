class Solution:
    def placeWordInCrossword(self, board: list[list[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        length = len(word)

        def check(r, c, dir):
            if(dir == 'h'):
                #forward
                matched = True
                for i in range(length):
                    if(board[r][c-i] == " "):
                        continue
                    if(board[r][c-i] != word[i]):
                        matched = False
                        break
                if(matched):
                    return True

                #backward
                matched = True
                for i in range(length):
                    if(board[r][c-i] == " "):
                        continue
                    if(board[r][c-i] != word[-(i+1)]):
                        matched = False
                        break
                if(matched):
                    return True
            else:
                #forward
                matched = True
                for i in range(length):
                    if(board[r-i][c] == " "):
                        continue
                    if(board[r-i][c] != word[i]):
                        matched = False
                        break
                if(matched):
                    return True

                #backward
                matched = True
                for i in range(length):
                    if(board[r-i][c] == " "):
                        continue
                    if(board[r-i][c] != word[-(i+1)]):
                        matched = False
                        break
                if(matched):
                    return True
            return False

        for r in range(row):
            count = 0
            for c in range(col):
                if(board[r][c] == '#'):
                    if(count == length and check(r, c-1, 'h')):
                        return True
                    else:
                        count = 0
                else:
                    count += 1
            if(count == length and check(r, col-1, 'h')):
                return True
        
        for c in range(col):
            count = 0
            for r in range(row):
                if(board[r][c] == '#'):
                    if(count == length and check(r-1, c, 'v')):
                        return True
                    else:
                        count = 0
                else:
                    count += 1
            if(count == length and check(row-1, c, 'v')):
                return True
        
        return False
        #TC O(m*n*length)