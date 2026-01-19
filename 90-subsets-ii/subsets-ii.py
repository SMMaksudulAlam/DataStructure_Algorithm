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
                s = ""
                for e in ar_:
                    s+=str(e)
                if(s not in dic):
                    dic[s] = 1
                    ans_.append(ar_)
            ans = ans_
        return ans