class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        1 --> 1
        2 --> 3
        3 --> 3+2+1 --> 6 
        4 --> 4+3+2+1 --> 10
        """
        l = 0
        r = 0
        ans = 0
        while(r<len(nums)):
            if(nums[r]==0):
                l = r
                while(r<len(nums) and nums[r]==0):
                    r+=1
                x = r-l
                ans += (x*(x+1))//2
            r+=1
        return ans