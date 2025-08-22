class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        mn = 0
        mx = sum(weights)

        def dayCount(cap):
            day = 1
            cur = 0
            for w in weights:
                if(w>cap):
                    return inf
                if(cur+w>cap):
                    day+=1
                    cur = 0
                cur+=w
            return day

        while(mn<=mx):
            #print(mn, mx)
            if(mn==mx):
                return mn
            if(mn+1==mx):
                if(dayCount(mn)<=days):
                    return mn
                return mx
            
            mid = (mn+mx)//2
            if(dayCount(mid)<=days):
                mx = mid
            else:
                mn = mid

        return -1