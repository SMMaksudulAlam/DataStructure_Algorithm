class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ln = len(nums)
        for i, e in enumerate(nums):
            if(e<=0):
                nums[i] = ln+1
        
        for i, e in enumerate(nums):
            e = abs(e)
            if(e<=ln):
                ind = e-1
                if(nums[ind]>0):
                    nums[ind] = -nums[ind]
        for i, e in enumerate(nums):
            if(e>0):
                return i+1
        return ln+1
        

                