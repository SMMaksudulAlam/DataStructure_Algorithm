class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hourCount(k):
            count = 0
            for e in piles:
                count += ceil(e/k)
            return count
        
        e = max(piles)
        s = 1
        k = -1
        while(s<=e):
            if(s==e):
                k = s
                break
            if(s+1==e):
                if(hourCount(s)<=h):
                    k = s
                else:
                    k = e
                break
            
            m = (s+e)//2
            if(hourCount(m)<=h):
                e = m
            else:
                s = m
        return k