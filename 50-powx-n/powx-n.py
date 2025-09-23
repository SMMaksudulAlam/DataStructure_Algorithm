class Solution:
    def myPow(self, x: float, n: int) -> float:
        if(x==0):
            return 0
        if(n==0):
            return 1
        
        neg = True if n<0 else False

        n = abs(n)
        ans = 1

        while(n>0):
            if(n%2==0):
                x*=x
                n/=2
            else:
                ans*=x
                n-=1
        
        if(neg):
            return 1.0/ans
            
        return ans