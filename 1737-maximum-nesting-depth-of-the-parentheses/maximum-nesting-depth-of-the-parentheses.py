class Solution:
    def maxDepth(self, s: str) -> int:
        op = 0
        ans = 0

        for ch in s:
            if(ch == '('):
                op+=1
            elif(ch == ')'):
                op-=1
            else:
                pass
            ans = max(ans, op)
        return ans
