class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        count = [1]*len(nums)

        for ind in range(len(nums)):
            for prev in range(ind):
                if(nums[ind]>nums[prev]):
                    if(dp[prev]+1>dp[ind]):
                        dp[ind] = dp[prev]+1
                        count[ind] = 0
                    if(dp[prev]+1==dp[ind]):
                        count[ind]+=count[prev]
        max_len = max(dp)
        ans = 0
        for i in range(len(dp)):
            if(dp[i]==max_len):
                ans += count[i]
        return ans
