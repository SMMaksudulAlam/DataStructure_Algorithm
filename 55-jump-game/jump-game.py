class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ans = [False]*len(nums)
        ans[0] = True
        for i, e in enumerate(nums):
            if(ans[i] == True):
                for j in range(e):
                    if(i+j+1 < len(nums)):
                        ans[i+j+1] = True
            if(ans[-1] == True):
                return True
        return False