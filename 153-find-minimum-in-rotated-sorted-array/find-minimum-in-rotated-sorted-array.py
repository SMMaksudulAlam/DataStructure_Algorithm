class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while(left<=right):
            left_e = nums[left]
            right_e = nums[right]

            if(left==right):
                return left_e
            if(left+1 == right):
                return min(left_e, right_e)

            mid = (left+right)//2
            mid_e = nums[mid]

            if(mid_e>right_e):
                left = mid
            else:
                right = mid
        return -1

