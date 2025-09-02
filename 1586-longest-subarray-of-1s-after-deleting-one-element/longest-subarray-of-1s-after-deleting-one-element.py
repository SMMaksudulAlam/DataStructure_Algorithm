class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count = -inf
        dic = {1:0, 0:0}
        l = 0
        for r in range(len(nums)):
            e = nums[r]
            dic[e]+=1
            while(dic[0]>1):
                e = nums[l]
                dic[e]-=1
                l+=1
            if(dic[0]==0):
                count = max(count, dic[1]-1)
            else:
                count = max(count, dic[1])
        return count
