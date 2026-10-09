class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        row = len(dungeon)
        col = len(dungeon[0])
        dp = {}
        def go(i, j):
            if((i, j) in dp):
                return dp[(i, j)]
            if(i==row-1 and j==col-1):
                if(dungeon[i][j]<=0):
                    return 1 - dungeon[i][j]
                else:
                    return 1
            ans = math.inf
            for di, dj in ((1, 0), (0, 1)):
                i_ = di+i
                j_ = dj+j
                if(0<=i_<row and 0<=j_<col):
                    status = dungeon[i][j]
                    ans = min(ans, -status+go(i_, j_))
            if(ans<=0):
                dp[(i, j)] = 1
                return 1
            dp[(i, j)] = ans
            return ans
        
        ans = go(0, 0)
        return ans
                    