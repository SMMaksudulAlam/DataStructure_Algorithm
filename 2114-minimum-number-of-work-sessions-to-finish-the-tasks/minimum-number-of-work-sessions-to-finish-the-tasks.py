class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        """
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

        #TC --> O(N * sessionTime * 2^N)
        """

        n = len(tasks)
        done = (1 << n) - 1
        mask = 0
        dp = {}
        def complete():
            nonlocal mask
            if(mask == done):
                return 1, 0

            if(mask in dp):
                return dp[mask]

            ans_session = n
            ans_occupied = sessionTime

            for i in range(n):
                if(mask & (1 << i) == 0):
                    mask |= (1 << i)
                    t = tasks[i]
                    sessions, occupied = complete()
                    if(occupied + t <= sessionTime):
                        if(sessions <= ans_session and occupied + t <= ans_occupied): #note, here we also need to compare the occupied time too to get the best state. (session: 5, occupied: 5) is a better state than (session: 5, occupied: 10) as the former one keeps more scope to add more tasks
                            ans_session = sessions
                            ans_occupied = occupied + t
                    else:
                        sessions += 1
                        if(sessions <= ans_session and t <= ans_occupied): #same for here
                            ans_session = sessions
                            ans_occupied = t

                    mask ^= (1 << i)
            
            dp[mask] = (ans_session, ans_occupied) #last time, error use due to copy-pasting, key remained as (mask, occupied), just like last version
            return ans_session, ans_occupied
        
        ans, occupied = complete()
        return ans
        
        #TC --> O(N*2^N)