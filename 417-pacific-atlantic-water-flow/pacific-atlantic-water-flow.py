class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p = set()
        s = set()
        for r in range(len(heights)):
            p.add((r, 0))
            s.add((r, 0))
        for c in range(len(heights[0])):
            p.add((0, c))
            s.add((0, c))

        
        dir = [(-1, 0), (1, 0), (0, -1,), (0, 1)]
        while(s):
            s_ = set()
            for i, j in s:
                for dx, dy in dir:
                    x = i+dx
                    y = j+dy
                    if(0<=x<len(heights) and 0<=y<len(heights[0]) and ((x, y) not in p) and heights[x][y]>=heights[i][j]):
                        s_.add((x, y))
                        p.add((x, y))
            s = s_
        #print(p)

        a = set()
        s = set()
        for r in range(len(heights)):
            a.add((r, len(heights[0])-1))
            s.add((r, len(heights[0])-1))
        for c in range(len(heights[0])):
            a.add((len(heights)-1, c))
            s.add((len(heights)-1, c))

        
        dir = [(-1, 0), (1, 0), (0, -1,), (0, 1)]
        while(s):
            s_ = set()
            for i, j in s:
                for dx, dy in dir:
                    x = i+dx
                    y = j+dy
                    if(0<=x<len(heights) and 0<=y<len(heights[0]) and ((x, y) not in a) and heights[x][y]>=heights[i][j]):
                        s_.add((x, y))
                        a.add((x, y))
            s = s_

        
        ans = []
        for x, y in p:
            if((x, y) in a):
                ans.append([x, y])
        return ans
