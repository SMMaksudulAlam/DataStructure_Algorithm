class Solution:
    def minArea(self, image: list[list[str]], x: int, y: int) -> int:
        """
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

        #TC --> O(m*n)
        """

        row = len(image)
        col = len(image[0])

        def row_has_black(r):
            for c in range(col):
                if(image[r][c] == "1"):
                    return True
            return False
        
        def col_has_black(c):
            for r in range(row):
                if(image[r][c] == "1"):
                    return True
            return False
        
        high_r = x
        low_r = x
        high_c = y
        low_c = y

        # search_left of y [0 -- y] --> low_col
        left = 0
        right = y

        while(left<=right):
            mid = (left+right)//2
            if(col_has_black(mid)):
                low_c = mid
                right = mid - 1
            else:
                left = mid + 1
        

        # search_right of y [y -- col-1] --> high_col
        left = y
        right = col-1

        while(left<=right):
            mid = (left+right)//2
            if(col_has_black(mid)):
                high_c = mid
                left = mid + 1
            else:
                right = mid - 1
        

        # search_top of x [0 -- x] --> low_row
        left = 0
        right = x

        while(left<=right):
            mid = (left+right)//2
            if(row_has_black(mid)):
                low_r = mid
                right = mid - 1
            else:
                left = mid + 1
        

        # search_down of x [x -- row-1] --> high_row
        left = x
        right = row-1

        while(left<=right):
            mid = (left+right)//2
            if(row_has_black(mid)):
                high_r = mid
                left = mid + 1
            else:
                right = mid - 1

        
        length = high_r - low_r + 1
        width = high_c - low_c + 1
        area = length * width

        return area