class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if(len(s)!=len(goal)):
            return False
        
        for i in range(len(s)):
            if(s[i]==goal[0]):
                s_ = s[i:] + s[:i]
                if(s_ == goal):
                    return True
        return False