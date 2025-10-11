class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        for r in range(1, len(mat)):
            for c in range(len(mat[0])):
                if(mat[r][c]==0):
                    pass
                else:
                    mat[r][c]+=mat[r-1][c]
        
        count = 0
        for r in range(len(mat)):
            for c in range(len(mat[0])-1, -1, -1):
                if(mat[r][c]==0):
                    continue
                
                local_count = mat[r][c]
                local_max = mat[r][c]
                for k in range(c-1, -1, -1):
                    if(mat[r][k]==0):
                        break
                    local_max = min(local_max, mat[r][k])
                    local_count += local_max

                count+=local_count
        return count
