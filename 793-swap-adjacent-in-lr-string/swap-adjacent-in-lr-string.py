class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        q = deque()
        for i, e in enumerate(start):
            if(e=='X'):
                continue
            q.append((e, i))

        for i, e in enumerate(result):
            if(e=='X'):
                continue
            if(e=='R'):
                if(q and q[0][0]=='R' and q[0][1]<=i):
                    q.popleft()
                    pass
                else:
                    return False
            if(e=='L'):
                if(q and q[0][0]=='L' and q[0][1]>=i):
                    q.popleft()
                    pass
                else:
                    return False
                    
        if(q):
            return False
        return True
            
