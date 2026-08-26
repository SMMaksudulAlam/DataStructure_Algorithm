class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 0
        if(nums[0]>nums[1]):
            return 0
        if(nums[-1]>nums[-2]):
            return len(nums)-1

        left = 0
        right = len(nums)-1

        while(left<=right):
            mid = (left+right)//2
            if(left == right or (nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid])):
                return mid
            if(nums[mid+1]>nums[mid]):
                left = mid+1
            else:
                right = mid-1
        return -1