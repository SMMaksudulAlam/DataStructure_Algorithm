class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        if(not nums or target<nums[0] or target>nums[-1]):
            return ans

        left = 0
        right = len(nums)-1
        left_ind = right
        while(left<=right):
            mid = (left+right)//2
            if(target <= nums[mid]):
                left_ind = mid
                right = mid-1
            else:
                left = mid+1
        
        if(nums[left_ind] == target):
            ans[0] = left_ind
        else:
            return ans
        
        left = left_ind
        right = len(nums)-1
        right_ind = left
        while(left<=right):
            mid = (left+right)//2
            if(target >= nums[mid]):
                right_ind = mid
                left = mid+1
            else:
                right = mid-1
        
        ans[1] = right_ind
        return ans