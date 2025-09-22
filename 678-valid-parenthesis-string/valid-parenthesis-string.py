class Solution:
    def checkValidString(self, s: str) -> bool:
        open = []
        star = []
        for i, e in enumerate(s):
            if(e=='('):
                open.append(i)
            elif(e=='*'):
                star.append(i)
            else:
                if(not open and not star):
                    return False
                if(open):
                    open.pop()
                else:
                    star.pop()
        if(len(open)>len(star)):
            return False
        
        while(open and star):
            if(open[-1]>star[-1]):
                return False
            open.pop()
            star.pop()
        
        return True

