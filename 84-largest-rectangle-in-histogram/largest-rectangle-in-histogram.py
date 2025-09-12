class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for r in range(len(heights)):
            h = heights[r]
            l = r
            while(stack and stack[-1][0]>=h):
                h_, l_, r_ = stack.pop()
                area = h_*(r-l_)
                ans = max(ans, area)
                l = l_
            area = h*(r-l+1)
            ans = max(ans, area)
            stack.append((h, l, r))

        if(stack):
            R = stack[-1][2]
            for (h_, l_, r_) in stack:
                area = h_*(R-l_+1)
                ans = max(ans, area)
        
        return ans
        

