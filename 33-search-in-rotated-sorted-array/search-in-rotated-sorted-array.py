class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while(left<=right):
            if(left == right):
                return left if nums[left]==target else -1
            if(left+1==right):
                if(nums[left]==target):
                    return left
                elif(nums[right]==target):
                    return right
                else:
                    return -1
            
            mid = (left+right)//2
            mid_val = nums[mid]

            if(nums[left]<=mid_val):
                if(nums[left]<=target<=mid_val):
                    right = mid
                else:
                    left = mid
            else:
                if(mid_val<=target<=nums[right]):
                    left = mid
                else:
                    right = mid
        return -1