class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = 0
        neg = 1

        ans = [0]*len(nums)

        for n in nums:
            if(n>0):
                ans[pos] = n
                pos+=2
            else:
                ans[neg] = n
                neg+=2

        return ans