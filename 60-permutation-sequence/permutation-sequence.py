class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i+1) for i in range(n)] #1, 2, 3, 4

        def facto(num):
            if(num == 0):
                return 1
            ans = 1
            for i in range(1, num+1):
                ans *= i
            return ans
        
        k-=1 #8
        ans = ""
        while(n>0):
            block = facto(n-1) #6 2 1
            ind = (k // block) #1 1  0
            num = nums[ind] #2 3 1
            ans += num #2 3 1
            nums.remove(num) #1, 3, 4 || 1, 4 || 4
            k %= block #2 0 0
            n-=1 #3 2 1
            
        return ans

