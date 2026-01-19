class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        dic = {}

        for n in nums:
            ans_ = []
            for ar in ans:
                ans_.append(ar)
                ar_ = ar+[n]
                s = ''.join([str(i) for i in ar_])
                if(s not in dic):
                    dic[s] = 1
                    ans_.append(ar_)
            ans = ans_
        return ans