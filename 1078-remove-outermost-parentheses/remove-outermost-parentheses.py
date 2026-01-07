class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        op = 0
        cl = 0
        q = deque()
        ans = ""
        for ch in s:
            if(ch == '('):
                q.append(ch)
                op+=1
            else:
                q.append(ch)
                cl+=1
            
            if(op==cl):
                q.popleft()
                q.pop()
                ans += ''.join(q)
                q = deque()
                op = 0
                cl = 0
        return ans


