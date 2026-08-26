class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def days_count(cap):
            ans = 0
            w_sum = 0
            for w in weights:
                if(w>cap):
                    return inf
                if(w_sum+w<=cap):
                    w_sum += w
                else:
                    ans+=1
                    w_sum = w
            return ans+1
        
        left = 1
        right = sum(weights)
        ans = right

        while(left<=right):
            mid = (left+right)//2
            d = days_count(mid)
            if(d<=days):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans