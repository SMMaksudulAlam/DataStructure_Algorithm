class Solution:
    def jump(self, nums: List[int]) -> int:

        count = 0
        limit = 0

        i=0
        while(True):
            j = i
            if(limit>=len(nums)-1):
                return count
            next_limit = limit
            while(j<=limit):
                next_limit = max(next_limit, j+nums[j])
                j+=1
            if(limit == next_limit):
                return -1
            limit = next_limit
            count+=1
        return -1
            
