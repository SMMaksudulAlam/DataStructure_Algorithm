import bisect
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        if(nums[-1]<target):
            return len(nums)

        while(l<=r):
            if(l==r):
                return l
            if(l+1==r):
                if(nums[l]>=target):
                    return l
                return r
            mid = (l+r)//2
            if(nums[mid]>=target):
                r = mid
            else:
                l = mid
        return -1