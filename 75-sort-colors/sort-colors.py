class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        while(z<len(nums) and nums[z]==0):
            z+=1
        
        t = len(nums)-1
        while(t>0 and nums[t]==2):
            t-=1
        
        cur = z
        while(cur<=t):
            num = nums[cur]
            if(num == 1):
                cur+=1
                continue
            if(num == 0):
                if(cur == z):
                    cur+=1
                else:
                    nums[z], nums[cur] = nums[cur], nums[z]
                z+=1
            if(num == 2):
                nums[t], nums[cur] = nums[cur], nums[t]
                t-=1
        return