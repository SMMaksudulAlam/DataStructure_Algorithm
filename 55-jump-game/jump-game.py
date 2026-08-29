class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
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
        """
        max_reach = 0
        curr = 0
        next_iteration = True
        while(next_iteration):
            next_iteration = False
            next_max_reach = max_reach
            while(curr<=max_reach):
                if(curr>=len(nums)-1):
                    return True
                next_max_reach = max(next_max_reach, curr + nums[curr])
                curr+=1
            if(next_max_reach>max_reach):
                next_iteration = True
                max_reach = next_max_reach
        return False


        