class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l2r = []
        r2l = deque([])

        #going from left to right
        storage = []

        for i, h in enumerate(heights):
            while(storage and storage[-1][0]>=h):
                storage.pop()

            if(not storage):
                l2r.append((-1))
                storage.append((h, i))
            else:
                l2r.append((storage[-1][1]))
                storage.append((h, i))

        #going from right to left
        storage = deque([])
        ln = len(heights)
        for i in range(ln-1, -1, -1):
            h = heights[i]
            while(storage and storage[0][0]>=h):
                storage.popleft()
                
            if(not storage):
                r2l.appendleft((ln))
                storage.appendleft((h, i))
            else:
                r2l.appendleft((storage[0][1]))
                storage.appendleft((h, i))

        #print(l2r, r2l)
        ans = 0
        for i in range(ln):
            h = heights[i]
            w = (i-l2r[i]) + (r2l[i]-i) - 1
            ans = max(ans, h*w)
        return ans
