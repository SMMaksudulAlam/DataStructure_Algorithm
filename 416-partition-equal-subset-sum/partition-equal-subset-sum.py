class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if(s%2==1):
            return False
        
        half = s//2

        @lru_cache(maxsize=None)
        def sub(target, ind):
            if(target==0):
                return True
            if(target<0 or ind<0):
                return False

            take = False
            if(target>=nums[ind]):
                take = sub(target-nums[ind], ind-1)
                if(take):
                    return True
            not_take = sub(target, ind-1)
            
            ans = not_take
            return ans
        
        return sub(half, len(nums)-1)