class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp = {}
        def lis(ind, prev_ind):
            if((ind, prev_ind) in dp):
                return dp[ind, prev_ind]
            if(ind==len(nums)):
                return 0
            n = nums[ind]
            take = 0
            if(prev_ind == -1 or nums[prev_ind]<nums[ind]):
                take = 1 + lis(ind+1, ind)
            not_take = lis(ind+1, prev_ind)

            ans = max(take, not_take)
            dp[(ind, prev_ind)] = ans
            return dp[(ind, prev_ind)]
        
        ans = lis(0, -1)
        return ans
        """
        ans = []
        for n in nums:
            ind = bisect.bisect_left(ans, n)
            if(ind == len(ans)):
                ans.append(n)
            else:
                ans[ind] = n
            #print(n, ans)
        return len(ans)
