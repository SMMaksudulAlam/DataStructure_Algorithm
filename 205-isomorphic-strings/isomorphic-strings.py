class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        dic1 = {}
        dic2 = {}
        for i in range(len(s)):
            ch1 = s[i]
            ch2 = t[i]

            if(ch1 in dic1):
                if(ch2 not in dic2):
                    return False
                if(dic1[ch1]!=ch2 or dic2[ch2]!=ch1):
                    return False
            elif(ch2 in dic2):
                return False
            else:
                dic1[ch1]=ch2
                dic2[ch2]=ch1
        return True