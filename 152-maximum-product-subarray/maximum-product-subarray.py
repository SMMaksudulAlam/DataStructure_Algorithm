class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = nums[0]
        mn = nums[0]
        ans = max(mx, mn)

        for i in range(1, len(nums)):
            e = nums[i]
            mx_ = max(e, mx*e, mn*e)
            mn = min(e, mx*e, mn*e)
            mx = mx_
            ans = max(ans, mx)

        return ans