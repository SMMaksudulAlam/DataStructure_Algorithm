class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        mn = 0
        mx = sum(nums)

        if(k==1):
            return mx
        
        def splitCount(cap):
            count = 1
            stotal = 0

            for e in nums:
                if(e>cap):
                    return inf
                
                if(stotal+e>cap):
                    stotal = 0
                    count+=1
                stotal += e

            return count
        
        while(mn<=mx):
            if(mn==mx):
                return mn
            if(mn+1==mx):
                if(splitCount(mn)<=k):
                    return mn
                return mx
            
            mid = (mn+mx)//2
            #print(mn, mx, mid, splitCount(mid))
            if(splitCount(mid)<=k):
                mx = mid
            else:
                mn = mid
            
        return -1