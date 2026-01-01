class Solution:
    def check(self, nums: List[int]) -> bool:
        if(len(nums)==1):
            return True
        fall = 0
        for i in range(1, len(nums)):
            if(nums[i]<nums[i-1]):
                fall+=1
        
        if(fall==0):
            return True
        
        if(fall>1):
            return False
        
        if(nums[-1]<=nums[0]):
            return True
            
        return False
