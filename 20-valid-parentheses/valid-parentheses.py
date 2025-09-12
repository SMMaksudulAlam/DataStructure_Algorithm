class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')': '(', '}': '{', ']': '['}

        for e in s:
            if(e in ['(', '{', '[']):
                stack.append(e)
            else:
                if(stack and stack[-1] == dic[e]):
                    stack.pop()
                else:
                    return False
        if(stack):
            return False
        return True
        