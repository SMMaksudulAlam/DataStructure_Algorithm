class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while(left<=right):
            mid = (left+right)//2

            if(left == right or (nums[mid-1]!= nums[mid] and nums[mid+1]!=nums[mid])):
                return nums[mid]
            
            if(mid%2==0):
                if(nums[mid+1] == nums[mid]):
                    left = mid+1
                else:
                    right = mid-1
            else:
                if(nums[mid-1] == nums[mid]):
                    left = mid+1
                else:
                    right = mid-1
        return -1