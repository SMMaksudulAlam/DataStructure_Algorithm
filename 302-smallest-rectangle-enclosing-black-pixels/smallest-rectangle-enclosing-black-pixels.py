class Solution:
    def minArea(self, image: list[list[str]], x: int, y: int) -> int:
        high_r = x
        low_r = x
        high_c = y
        low_c = y

        dir = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        row = len(image)
        col = len(image[0])

        visited = set()

        def dfs(r, c):
            nonlocal high_r, low_r
            nonlocal high_c, low_c

            if((r, c) in visited):
                return
            
            visited.add((r, c))

            if(r<low_r):
                low_r = r
            if(r>high_r):
                high_r = r
            if(c<low_c):
                low_c = c
            if(c>high_c):
                high_c = c

            for dr, dc in dir:
                r_ = r+dr
                c_ = c+dc

                if(0<=r_<row and 0<=c_<col and image[r_][c_] == "1"):
                    dfs(r_, c_)
            return
        
        dfs(x, y)
        length = high_r - low_r + 1
        width = high_c - low_c + 1
        area = length * width

        return area
            
