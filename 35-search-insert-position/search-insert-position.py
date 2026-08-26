import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(target <= nums[0]):
            return 0
        if(target > nums[-1]):
            return len(nums)
        
        left = 0
        right = len(nums)-1
        ans = right
        while(left<=right):
            mid = (left+right)//2
            if(target <= nums[mid]):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans