class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(not nums):
            return [-1, -1]
        
        ind = bisect_left(nums, target)

        if(ind == len(nums)):
            return [-1, -1]
        
        if(nums[ind]!=target):
            return [-1, -1]
        
        return[ind, bisect_right(nums, target)-1]