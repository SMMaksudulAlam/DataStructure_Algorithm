class Solution:
    def jump(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return 0
        ans = [0]*len(nums)
        ans[0] = 1
        for i in range(1, min(nums[0]+1, len(ans))):
            ans[i] = 1

        for i in range(1, len(nums)):
            if(ans[i]>0):
                jmp = nums[i]
                for j in range(i+1, min(len(ans), i+jmp+1)):
                    if(ans[j]==0):
                        ans[j] = ans[i]+1
                    else:
                        ans[j] = min(ans[j], ans[i]+1)
        return ans[-1]

        