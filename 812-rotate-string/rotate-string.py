class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s)!=len(goal)):
            return False
        s+=s
        ln = len(goal)
        for i in range(ln):
            if(s[i:i+ln]==goal):
                return True
        return False
