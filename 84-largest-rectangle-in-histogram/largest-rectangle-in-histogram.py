class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l2r = []
        stack = []
        for i in range(len(heights)):
            e = heights[i]
            while(stack and stack[-1][0]>=e):
                stack.pop()
            if(not stack):
                l2r.append(-1)
            else:
                l2r.append(stack[-1][1])
            stack.append((e, i))

        r2l = deque()
        q = deque()
        for i in range(len(heights)-1, -1, -1):
            e = heights[i]
            while(q and q[0][0]>=e):
                q.popleft()
            if(not q):
                r2l.appendleft(len(heights))
            else:
                r2l.appendleft(q[0][1])
            q.appendleft((e, i))
        
        ans = 0

        for i in range(len(heights)):
            h = heights[i]
            l = i - l2r[i]
            r = r2l[i] - i

            ans = max(ans, h*(l+r-1))
        return ans
        

