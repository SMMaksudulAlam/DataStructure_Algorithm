class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def time(k):
            t = 0
            for p in piles:
                t += math.ceil(p/k)
            return t

        min_b = 1
        max_overall = max_b = max(piles)

        while(min_b<=max_b):
            if(min_b == max_b):
                return min_b

            if(min_b+1 == max_b):
                if(time(min_b)<=h):
                    return min_b
                else:
                    return max_b
            

            mid_b = (min_b + max_b) // 2

            if(time(mid_b) <= h):
                max_b = mid_b
            else:
                min_b = mid_b
        
        return max_overall