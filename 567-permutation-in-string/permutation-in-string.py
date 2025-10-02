class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False

        dic = {}
        for e in s1:
            dic[e] = dic.get(e, 0)+1
        
        l = 0
        for r in range(len(s2)):
            if(s2[r] not in dic):
                while(l<=r):
                    if(s2[l] in dic):
                        dic[s2[l]]+=1
                    l+=1
            else:
                while(dic[s2[r]]<=0):
                    if(s2[l] in dic):
                        dic[s2[l]]+=1
                    l+=1
                dic[s2[r]] -= 1
                if(max(dic.values())==0):
                    return True
        return False

