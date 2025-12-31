class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        mx = nums[0]
        mn = nums[0]
        for i, n in enumerate(nums):
            if(i==0):
                continue
            if(n==0):
                mx = 0
                mn = 0
                ans = max(ans, 0)
            else:
                temp_mx = max(n, mx*n, mn*n)
                mn = min(n, mx*n, mn*n)
                mx = temp_mx
                ans = max(ans, mx)
        return ans