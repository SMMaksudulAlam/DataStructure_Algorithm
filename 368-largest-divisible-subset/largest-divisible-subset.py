class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        """
        nums.sort()
        ans = []
        def lds(ind, ar):
            nonlocal ans
            if(ind == len(nums)):
                if(len(ans)<len(ar)):
                    ans = ar
                return
            n = nums[ind]
            if(not ar or (n % ar[-1] == 0)):
                lds(ind+1, ar+[n])
            lds(ind+1, ar)
            return 
        lds(0, [])
        return ans
        """

        nums.sort()
        dp = [1]*len(nums)
        ans = 0
        ans_ind = -1
        track = [-1]*len(nums)
        
        for ind in range(len(nums)):
            for prev in range(ind):
                if(nums[ind]%nums[prev]==0):
                    if(dp[ind] < dp[prev]+1):
                        dp[ind] = dp[prev]+1
                        track[ind] = prev
                        #print(">>>>>", track, ind, prev)
            if(ans<dp[ind]):
                ans = dp[ind]
                ans_ind = ind
                
        lis_array = []
        #print(nums)
        #print(dp, track)
        while(ans_ind != -1):
            lis_array.append(nums[ans_ind])
            ans_ind = track[ans_ind]
            
        lis_array = lis_array[::-1]
        return lis_array