class Solution:
    def removeOnes(self, grid: list[list[int]]) -> bool:
        s = ""
        f_s = ""
        for n in grid[0]:
            if(n==0):
                s+='0'
                f_s+='1'
            else:
                f_s+='0'
                s+='1'
        
        for row in grid:
            temp = ""
            for c in row:
                if(c==1):
                    temp+='1'
                else:
                    temp+='0'
            if(temp != s and temp != f_s):
                return False
        return True

            