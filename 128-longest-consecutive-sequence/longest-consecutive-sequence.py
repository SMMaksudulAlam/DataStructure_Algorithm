class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0
        for n in s:
            if(n+1 not in s):
                ln = 0
                cur = n
                while(cur in s):
                    ln+=1
                    cur-=1
                ans = max(ans, ln)
        return ans

