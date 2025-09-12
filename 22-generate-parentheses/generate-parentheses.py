class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(s, op, cl):
            nonlocal n
            if(op==n and cl==n):
                ans.append(s)
                return
            if(op<n):
                dfs(s+'(', op+1, cl)
            if(cl<op):
                dfs(s+')', op, cl+1)
        
        dfs("", 0 , 0)
        return ans