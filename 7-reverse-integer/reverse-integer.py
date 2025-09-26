class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        p_inf = 2**31-1
        n_inf = -2**31

        if(x<0):
            x*=-1
            neg = True
        
        ans = 0
        while(x>0):
            ans = ans*10 + x%10
            x //= 10
        
        if(neg):
            ans*=-1

        return ans if n_inf<=ans<=p_inf else 0