class Solution:
    def findMin(self, nums: List[int]) -> int:        
        left = 0
        right = len(nums)-1

        while(left<=right):
            mid = (left+right)//2
            if(left == right or nums[mid-1]>nums[mid] and nums[mid]<nums[mid+1]):
                return nums[mid]

            if(nums[left]<nums[right]):
                return nums[left]
                
            if(nums[left]<=nums[mid]):
                left = mid+1
            else:
                right = mid-1

        return -1