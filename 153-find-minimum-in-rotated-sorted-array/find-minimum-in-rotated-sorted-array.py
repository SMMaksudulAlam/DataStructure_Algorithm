class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        if(len(nums)==2):
            return min(nums)

        if(nums[-1]>nums[0] and nums[0]<nums[1]):
            return nums[0]
        if(nums[-2]>nums[-1] and nums[-1]<nums[0]):
            return nums[-1]
        
        left = 0
        right = len(nums)-1

        while(left<=right):
            mid = (left+right)//2
            if(nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]):
                return nums[mid]

            if(nums[left]<nums[right]):
                return nums[left]
                
            if(nums[left]<=nums[mid]):
                left = mid+1
            else:
                right = mid-1

        return -1