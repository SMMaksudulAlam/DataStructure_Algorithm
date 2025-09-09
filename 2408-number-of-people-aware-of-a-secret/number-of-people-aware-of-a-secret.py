class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        ans = [0]*n
        ans[0] = 1
        mod = 10**9+7
        for i in range(n):
            if(ans[i]!=0):
                for ind in range(i+delay, min(i+forget, n)):
                    ans[ind] = (ans[ind]+ans[i]) % mod
            #print(i, ans)
        count = 0
        for i in range(1, forget+1):
            count =  (count + ans[-i]) % mod

        return count
