class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        
        left = 0
        right = len(nums)-1

        while(left<=right):
            if(left==right):
                return nums[left]
            if(left+1==right):
                if(left%2==1 and nums[left]==nums[left-1]):
                    return nums[right]
                return nums[left]
            
            mid = (left+right)//2
            if(mid%2==1):
                if(nums[mid]==nums[mid-1]):
                    left=mid
                else:
                    right = mid
            else:
                if(nums[mid]==nums[mid+1]):
                    left=mid
                else:
                    right = mid
                    
        return -1