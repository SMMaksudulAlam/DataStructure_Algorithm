class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dp = {}
        
        def traverse(left_ind, right_ind, r):
            if((left_ind, right_ind, r) in dp):
                return dp[(left_ind, right_ind, r)]
            if(r>=row):
                return 0
            left = 0
            right = 0

            if(left_ind != right_ind):
                left = grid[r][left_ind]
            right = grid[r][right_ind]

            temp_ans = 0
            for i in [-1, 0, 1]:
                left_ind_next = left_ind + i
                if(0<=left_ind_next<col):
                    for j in [-1, 0, 1]:
                        right_ind_next = right_ind + j
                        if(0<=right_ind_next<col):
                            temp_ans = max(temp_ans, traverse(left_ind_next, right_ind_next, r+1))
            
            dp[(left_ind, right_ind, r)] = left+right+temp_ans
            return left+right+temp_ans

        ans = traverse(0, col-1, 0)
        return ans