class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if(nums[0] == target or nums[-1]==target):
            return True

        left = 0
        right = len(nums)-1

        while(left<=right):
            mid = (left+right)//2
            if(nums[mid]==target or nums[left]==target or nums[right]==target):
                return True
            
            if(nums[left]<=nums[mid]<=nums[right]):
                left+=1
                right-=1
                continue
            
            if(nums[left]>nums[mid]):
                if(target>nums[left] or target<nums[mid]):
                    right = mid-1
                else:
                    left = mid+1
            else:
                if(target>nums[mid] or target<nums[right]):
                    left = mid+1
                else:
                    right = mid-1
        return False