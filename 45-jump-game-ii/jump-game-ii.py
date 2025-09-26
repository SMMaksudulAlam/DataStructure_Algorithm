class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = [-1]*len(nums)
        ans[0] = 0
        for i in range(len(nums)):
            if(nums[i]!=-1):
                for nxt in range(i+1, min(len(nums), i+nums[i]+1)):
                    if(ans[nxt]==-1):
                        ans[nxt] = ans[i]+1
                    else:
                        ans[nxt] = min(ans[i]+1, ans[nxt])
        return ans[-1]