class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        q = deque()
        ans = []
        for i in range(len(temperatures)-1, -1, -1):
            while(q and temperatures[q[0]]<=temperatures[i]):
                q.popleft()
            if(not q):
                ans.append(0)
            else:
                ans.append(q[0]-i)
            q.appendleft(i)

        ans_ = []
        for i in range(len(ans)-1, -1, -1):
            ans_.append(ans[i])
        return ans_
        
