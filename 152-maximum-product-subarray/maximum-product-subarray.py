class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = nums[0]
        mn = nums[0]
        
        ans = max(mx, mn)

        for i in range(1, len(nums)):
            e = nums[i]
            if(e==0):
                mn = 0
                mx = 0
            else:
                mx_ = max(e, mn*e, mx*e)
                mn_ = min(e, mn*e, mx*e)

                mx = mx_
                mn = mn_
            
            ans = max(ans, mx)

        return ans