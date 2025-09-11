class Solution:
    def sortVowels(self, s: str) -> str:
        v = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

        v_ = []
        for e in s:
            if(e in v):
                v_.append(e)
        
        v_.sort()
        s_ = ""
        i = 0
        for e in s:
            if(e in v):
                s_+=v_[i]
                i+=1
            else:
                s_+=e
        return s_