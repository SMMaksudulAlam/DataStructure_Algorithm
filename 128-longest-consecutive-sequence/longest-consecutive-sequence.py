class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic = {}
        for e in nums:
            dic[e] = 1
        mx = 0
        for e in dic.keys():
            count = 1
            if(e+1 not in dic):
                while(e-1 in dic):
                    count += 1
                    e = e-1
                mx = max(mx, count)
        return mx
        