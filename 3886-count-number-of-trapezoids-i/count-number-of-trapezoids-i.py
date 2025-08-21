class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        dic = {}
        for x, y in points:
            dic[y] = dic.get(y, 0)+1
        
        keys = list(dic.keys())

        count = 0
        mod = 10**9+7
        sidesInaLine = []
        sm = 0
        for i in range(len(keys)):
            p1 = dic[keys[i]]
            if(p1<2):
                continue
            pp1 = (p1*(p1-1))//2
            sidesInaLine.append(pp1)
            sm+=pp1
        
        ln = len(sidesInaLine)
        for s in sidesInaLine:
            ss = sm-s
            count = (count+(s*ss))%mod
            sm-=s
        return count
                

