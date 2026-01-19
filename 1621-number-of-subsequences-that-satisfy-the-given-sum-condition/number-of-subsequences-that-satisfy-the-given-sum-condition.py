class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        ans = 0
        nums.sort()
        left = 0
        mod = 10**9 + 7
        right = len(nums)-1
        
        while(left<=right):
            if(nums[left]+nums[left] > target):
                return ans
            
            if(nums[left]+nums[right]>target):
                right-=1
            
            else:
                count = right-left
                ans = (ans + (2**count)%mod)%mod
                left+=1
            
        return ans
