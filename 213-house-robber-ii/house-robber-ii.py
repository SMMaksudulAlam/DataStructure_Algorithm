class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums)<=3):
            return max(nums)
    
        ans1 = nums[:]
        ans1.pop()
        ans1[2]+=ans1[0]

        for i in range(3, len(ans1)):
            ans1[i]+=max(ans1[i-2], ans1[i-3])

        
        ans2 = nums[1:]
        ans2[2]+=ans2[0]
        for i in range(3, len(ans1)):
            ans2[i]+=max(ans2[i-2], ans2[i-3])
        
        return max(max(ans1), max(ans2))