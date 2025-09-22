class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if(len(nums)==1):
            return True
        mx = 0
        for i, e in enumerate(nums):
            if(e==0):
                if(mx == i):
                    return False
            mx = max(mx, i+e)
            if(mx>=len(nums)-1):
                return True
        return False