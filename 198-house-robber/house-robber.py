class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)<=2):
            return max(nums)
        if(len(nums)==3):
            return max(nums[0]+nums[2], nums[1])
        
        right = nums[0]+nums[2]
        mid = nums[1]
        left = nums[0]

        ans = max(right, mid)

        for i in range(3, len(nums)):
            temp = right
            right = nums[i] + max(mid, left)
            mid, left = temp, mid
            ans = max(ans, right, mid)
        
        return ans
