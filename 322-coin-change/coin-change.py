class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [0]*(amount+1)
        ans[0] = 1

        for i in range(amount+1):
            for c in coins:
                if(i-c>=0 and ans[i-c]!=0):
                    if(ans[i]==0):
                        ans[i] = ans[i-c]+1
                    else:
                        ans[i] = min(ans[i], ans[i-c]+1)
        return ans[amount]-1
