class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf
        sm = 0
        for n in nums:
            if(sm>0):
                sm+=n
            else:
                sm = n
            ans = max(ans, sm)
        return ans