class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vCount = 0
        v = {'a', 'e', 'i', 'o', 'u'}
        for e in s:
            if(e in v):
                vCount+=1
        if(vCount==0):
            return False
        return True