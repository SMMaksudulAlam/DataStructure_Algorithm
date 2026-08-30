class Solution:
    def checkValidString(self, s: str) -> bool:
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
