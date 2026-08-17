class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = pos = neg = nums[0]
        for n in nums[1:]:
            if(n==0):
                pos = 0
                neg = 0
            else:
                pos_ = pos
                pos = max(n, pos*n, neg*n)
                neg = min(n, pos_*n, neg*n)
            ans = max(ans, n, pos, neg)
        return ans