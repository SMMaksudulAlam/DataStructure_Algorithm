class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {}
        ans = 0
        l = 0
        for r, e in enumerate(fruits):
            if(len(dic.keys())<2):
                dic[e] = dic.get(e, 0)+1
            else:
                if(e in dic):
                    dic[e] = dic.get(e, 0)+1
                else:
                    while(len(dic.keys())==2):
                        e_ = fruits[l]
                        dic[e_] -=1
                        if(dic[e_] == 0):
                            del dic[e_]
                        l+=1
                    dic[e] = dic.get(e, 0)+1
            ans = max(ans, sum(dic.values()))

        return ans