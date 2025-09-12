class Solution:
    def findMin(self, nums: List[int]) -> int:
        if(len(nums)==1 or nums[0]<nums[-1]):
            return nums[0]
        
        s = 0
        e = len(nums)-1

        while(s<=e):
            if(s==e):
                return nums[s]
            if(s+1==e):
                return min(nums[s], nums[e])
            
            m = (s+e)//2

            if(nums[m]<nums[e]):
                e = m
            else:
                s = m

        return -1