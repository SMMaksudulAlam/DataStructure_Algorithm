class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        dp = {}
        def check(left, right, ind):
            if(right>left):
                return False
            if(ind>=len(s)):
                if(left == right):
                    return True
                return False
            if((left, right, ind) in dp):
                return dp[(left, right, ind)]
            ans = False
            if(s[ind] == '('):
                ans = ans or check(left+1, right, ind+1)
            elif(s[ind] == ')'):
                if(right<left):
                    ans = ans or check(left, right+1, ind+1)
            else:
                ans = ans or check(left+1, right, ind+1) or check(left, right+1, ind+1) or check(left, right, ind+1)
            
            dp[(left, right, ind)] = ans
            return ans
        
        ans = check(0, 0, 0)
        return ans
        """
        asteric = []
        left = []
        right = []
        for i, ch in enumerate(s):
            if(ch == '('):
                left.append(i)
            elif(ch == '*'):
                asteric.append(i)
            else:
                if(left):
                    left.pop()
                elif(asteric):
                    asteric.pop()
                else:
                    return False

        while(left and asteric):
            if(left[-1]<asteric[-1]):
                left.pop()
                asteric.pop()
            else:
                return False
        if(left):
            return False
            
        return True
            