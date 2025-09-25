class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [[-1, -1] for i in range (len(nums))]
        h_count = 0
        h_ind = 0
        for i, e in enumerate(nums):
            dp[i] = [i, 1]
            for j in range(i-1, -1, -1):
                if(e%nums[j]==0):
                    if(dp[j][1]+1>dp[i] [1]):
                        dp[i] = [j, dp[j][1]+1]
                        if(dp[i][1]>h_count):
                            h_count = dp[i][1]
                            h_ind = i
        ans = deque()
        while(dp[h_ind][0]!=h_ind):
            ans.appendleft(nums[h_ind])
            h_ind = dp[h_ind][0]
        ans.appendleft(nums[h_ind])
        return list(ans)
        