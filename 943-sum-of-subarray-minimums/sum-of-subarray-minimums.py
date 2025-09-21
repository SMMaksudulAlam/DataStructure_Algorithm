class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        l2r = []
        stack = []
        mod = 10**9+7


        for i, e in enumerate(arr):
            while(stack and stack[-1][0]>e):
                stack.pop()
            
            if(not stack):
                l2r.append(-1)
            else:
                l2r.append(stack[-1][1])
            
            stack.append((e, i))
        
        r2l = deque([])
        q = deque([])
        for i in range(len(arr)-1, -1, -1):
            e = arr[i]
            while(q and q[0][0]>=e):
                q.popleft()
            if(not q):
                r2l.appendleft(len(arr))
            else:
                r2l.appendleft(q[0][1])
            
            q.appendleft((e, i))
        
        #print(l2r, r2l)

        ans = 0
        for i in range(len(arr)):
            ans = (ans + (arr[i]*(i-l2r[i])*(r2l[i]-i))%mod)%mod
            #print(arr[i], ans)
        return ans
        
        
            

        