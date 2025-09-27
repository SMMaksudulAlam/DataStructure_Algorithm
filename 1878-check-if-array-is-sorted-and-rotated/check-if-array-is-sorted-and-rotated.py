class Solution:
    def check(self, nums: List[int]) -> bool:
        flop_count = 0
        for i in range(len(nums)-1):
            if(nums[i]>nums[i+1]):
                flop_count+=1
            if(flop_count>1):
                return False
        if(flop_count == 1):
            if(nums[0]<nums[-1]):
                return False
        return True