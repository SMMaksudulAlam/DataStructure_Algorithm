class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        dic = {}
        lst = [[]]
        
        for n in nums:
            lst_ = []
            for ls in lst:
                lst_.append(ls)
                ls_ = ls+[n]
                s = "".join([str(i) for i in ls_])
                if(s not in dic):
                    lst_.append(ls_)
                    dic[s]=1
            lst = lst_

        return lst