class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        for i, e in enumerate(nums):
            if(e==1):
                if(i==0):
                    count = 1
                else:
                    if(nums[i-1]==1):
                        count+=1
                    else:
                        count = 1
            maxCount = max(maxCount, count)
        return maxCount