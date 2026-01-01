class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums)-1

        while(left<=right):
            if(left == right):
                return True if nums[left]==target else False
            if(left+1==right):
                if(nums[left]==target):
                    return True
                elif(nums[right]==target):
                    return True
                else:
                    return False
            
            mid = (left+right)//2
            mid_val = nums[mid]
            left_unrotated = True
            for i in range(left+1, mid+1):
                if(nums[i]<nums[i-1]):
                    left_unrotated = False
                    break

            if(nums[left]<=mid_val and left_unrotated):
                if(nums[left]<=target<=mid_val):
                    right = mid
                else:
                    left = mid
            else:
                if(mid_val<=target<=nums[right]):
                    left = mid
                else:
                    right = mid
        return False