class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)<=2):
            return max(nums)
        
        prev, cur = nums[0], max(nums[1], nums[0])
        for i in range(2, len(nums)):
            nxt = max(nums[i]+prev, cur)
            prev, cur = cur, nxt

        return cur
