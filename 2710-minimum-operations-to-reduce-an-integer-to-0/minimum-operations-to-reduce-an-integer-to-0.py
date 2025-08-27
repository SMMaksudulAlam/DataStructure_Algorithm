class Solution:
    def minOperations(self, n: int) -> int:
        if(n==1 or n==2):
            return 1
        
        ar = []
        p = 0
        while(2**p<n):
            ar.append(2**p)
            p+=1
        ar.append(2**p)
        
        count = 0

        def build(n, c):
            if(n==0):
                return c
            ind = bisect.bisect_left(ar, n)
            if(ar[ind]==n):
                return c+1
            if(n-ar[ind-1]<=ar[ind]-n):
                return build(n-ar[ind-1], c+1)
            else:
                return build(ar[ind]-n, c+1)
            

        ans = build(n, 0)
        return ans
            

