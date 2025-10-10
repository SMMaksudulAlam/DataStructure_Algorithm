class Solution:
    def canJump(self, nums: List[int]) -> bool:
        limit = 0
        i = 0
        while(True):
            if(limit>=len(nums)-1):
                return True
            next_limit = limit
            while(i<=limit):
                next_limit = max(next_limit, i+nums[i])
                i+=1
            if(limit==next_limit):
                return False
            limit = next_limit
        return False