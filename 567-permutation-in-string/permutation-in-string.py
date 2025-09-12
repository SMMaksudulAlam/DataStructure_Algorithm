class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}
        if(len(s1)>len(s2)):
            return False
        
        for e in s1:
            dic[e] = dic.get(e, 0) + 1
        
        l = 0
        for r in range(len(s2)):
            if(s2[r] not in dic):
                while(l<r):
                    ch = s2[l]
                    if(ch in dic):
                        dic[ch]+=1
                    l+=1
            else:
                ch = s2[r]
                x = dic[ch]
                x-=1
                while(dic[ch]<1):
                    c = s2[l]
                    if(c in dic):
                        dic[c]+=1
                    l+=1

                x = dic[ch]
                x-=1
                dic[ch] = x
            
            print(l, r, dic)
            if(max(dic.values())==0):
                print(l, r, dic)
                return True
        return False
        