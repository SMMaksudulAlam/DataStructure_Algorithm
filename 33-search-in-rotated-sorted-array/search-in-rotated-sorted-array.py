class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while(left<=right):
            left_e = nums[left]
            right_e = nums[right]

            if(left==right):
                if(left_e == target):
                    return left
                else:
                    return -1

            if(left+1 == right):
                if(left_e == target):
                    return left
                elif(right_e == target):
                    return right
                else:
                    return -1 

            mid = (left+right)//2
            mid_e = nums[mid]

            if(left_e<mid_e):
                if(left_e<=target<=mid_e):
                    right = mid
                else:
                    left = mid
            else:
                if(mid_e<=target<=right_e):
                    left = mid
                else:
                    right = mid
        return -1