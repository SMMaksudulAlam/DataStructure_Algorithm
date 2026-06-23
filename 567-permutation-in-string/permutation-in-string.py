class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)):
            return False
        
        dic = {}
        for e in s1:
            dic[e] = dic.get(e, 0)+1
        
        left = 0
        for right in range(len(s2)):
            if(s2[right] in dic):
                dic[s2[right]] -= 1
            
            if(s2[right] not in dic):
                while(left<right):
                    if(s2[left] in dic):
                        dic[s2[left]] += 1
                    left+=1
            
            while(min(dic.values())<0):
                if(s2[left] in dic):
                    dic[s2[left]] += 1
                left+=1

            val = dic.values()
            if(max(val)==0 and min(val)==0):
                return True
        print(left, right, dic)
        return False
            

        