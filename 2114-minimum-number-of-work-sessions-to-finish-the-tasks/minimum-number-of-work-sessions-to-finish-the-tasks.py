class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        n = len(tasks)
        done = (1 << n) - 1
        mask = 0
        dp = {}
        def complete(occupied):
            nonlocal mask
            if(mask == done):
                return 1

            if((mask, occupied) in dp):
                return dp[(mask, occupied)]

            ans = n
            for i in range(n):
                if(mask & (1 << i) == 0):
                    mask |= (1 << i)
                    t = tasks[i]
                    if(t + occupied <= sessionTime):
                        ans = min(ans, complete(occupied+t))
                    else:
                        ans = min(ans, 1 + complete(t))
                    mask ^= (1 << i)
            
            dp[(mask, occupied)] = ans
            return ans
        
        return complete(0)