class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def fact(n):
            ans = 1
            for i in range(1, n+1):
                ans*=i
            return ans
        ar = [i for i in range(1, n+1)]

        f = fact(n+1) #24 #6 #2
        def build(n, k):#4, 9
            s = ""
            nonlocal f
            while(n>0):
                f = f//(n+1)
                seg_size = f//n #6 #2 #1
                ind = k//seg_size #1 #1 
                if(k%seg_size==0):
                    ind -= 1     
                s+=str(ar[ind]) #2 #3
                ar.remove(ar[ind]) #[1,3,4] #[1, 4]
                n-=1 #3 #2
                k = k%seg_size #3 #1
            return s

        s = build(n, k)
        return s

