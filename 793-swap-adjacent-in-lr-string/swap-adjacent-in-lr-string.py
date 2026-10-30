class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        r_ind = deque([])
        l_ind = deque([])

        for i, e in enumerate(start):
            if(e == 'L'):
                l_ind.append(i)
            if(e=='R'):
                r_ind.append(i)

        for i, e in enumerate(result):
            if(e == 'L'):
                if(l_ind and l_ind[0]>=i):
                    if(r_ind and r_ind[0]<l_ind[0]):
                            return False
                    l_ind.popleft()
                    continue
                else:
                    return False
            if(e=='R'):
                if(r_ind and r_ind[0]<=i):
                    if(l_ind and l_ind[0]<=i):
                            return False
                    r_ind.popleft()
                    continue
                else:
                    return False

        if(r_ind or l_ind):
            return False
        return True



