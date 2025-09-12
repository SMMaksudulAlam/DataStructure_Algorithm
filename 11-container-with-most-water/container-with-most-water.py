class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l = 0
        r = len(height)-1

        while(l<r):
            h1 = height[l]
            h2 = height[r]
            h = min(h1, h2)

            d = (r-l)

            area = d*h
            ans = max(ans, area)

            if(h1>h2):
                r-=1
            else:
                l+=1
        return ans
        