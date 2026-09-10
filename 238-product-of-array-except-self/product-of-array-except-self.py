class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        l2r = [0]*len(nums)
        r2l = [0]*len(nums)
        
        l2r[0] = nums[0]
        r2l[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            l2r[i] = l2r[i-1]*nums[i]
        
        for i in range(len(nums)-2, -1, -1):
            r2l[i] = r2l[i+1]*nums[i]
        

        ans = [r2l[1]]
        for i in range(1, len(nums)-1):
            ans.append(l2r[i-1]*r2l[i+1])
        ans.append(l2r[-2])

        return ans
        """
        
        ans = [0]*len(nums)
        pref = 1
        for i in range(len(nums)):
            ans[i] = pref
            pref *= nums[i]
        
        suff = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suff
            suff *= nums[i]
        
        return ans

