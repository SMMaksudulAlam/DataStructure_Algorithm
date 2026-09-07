class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if(s%2==1):
            return False
        
        half = s//2

        dp = [False]*(half+1)
        dp[0] = True
        for num in nums:
            dp_ = [False]*(half+1)
            dp_[0] = True
            for ind in range(1, half+1):
                dp_[ind] = dp[ind]
                if(ind-num>=0):
                    dp_[ind] = dp_[ind] or dp[ind-num]
            dp = dp_
        
        return dp[-1]