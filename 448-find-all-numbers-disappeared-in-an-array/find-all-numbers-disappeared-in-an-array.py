class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            e = abs(nums[i])
            ind = e-1
            if(nums[ind]>0):
                nums[ind] = -nums[ind]
        
        ans = []
        for i in range(len(nums)):
            if(nums[i]>0):
                ans.append(i+1)
        return ans