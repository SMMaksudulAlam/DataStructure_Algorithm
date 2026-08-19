class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights: List[int]) -> int:
            q = deque([])
            min_right = deque([])
            for i in range(len(heights)-1, -1, -1):
                n = heights[i]
                while(q and q[0][0]>=n):
                    q.popleft()
                if(not q):
                    min_right.appendleft(len(heights))
                else:
                    min_right.appendleft(q[0][1])
                q.appendleft((n, i))

            q = deque([])
            min_left = deque([])
            for i in range(len(heights)):
                n = heights[i]
                while(q and q[-1][0]>n):
                    q.pop()
                if(not q):
                    min_left.append(-1)
                else:
                    min_left.append(q[-1][1])
                q.append((n, i))

            max_area = 0

            for i in range(len(heights)):
                left = (i - min_left[i])
                right = (min_right[i]-i)
                max_area = max(max_area, (heights[i]*(left+right-1)))
            return max_area

        row = len(matrix)
        col = len(matrix[0])
        ans = 0

        prev = [0]*col

        for r in range(row):
            cur = [0]*col
            for c in range(col):
                ch = matrix[r][c]
                if(ch == "1"):
                    cur[c] = prev[c]+1
                else:
                    pass
            ans = max(ans, largestRectangleArea(cur))
            prev = cur
        return ans
