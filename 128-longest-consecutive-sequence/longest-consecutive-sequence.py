class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for e in nums:
            dic[e] = 1

        ans = 0
        for e in dic.keys():
            if(e+1 not in dic):
                count = 0
                cur = e
                while(cur in dic):
                    count+=1
                    cur -= 1
                ans = max(count, ans)
        return ans