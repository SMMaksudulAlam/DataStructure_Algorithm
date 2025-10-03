class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if(s%2!=0):
            return False
        
        ss = s//2

        ans = [[0]*(ss+1) for _ in range(len(nums)+1)]
        ans[0][0] = 1

        for i in range(1, len(nums)+1):
            e = nums[i-1]
            for j in range(ss+1):
                ans[i][j] = ans[i-1][j]
                if(j-e>=0):
                    ans[i][j] += ans[i-1][j-e]
                if(ans[-1][-1]!=0):
                    return True
        return False