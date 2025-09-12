class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = [0]*n
        l = 0
        lh = height[0]
        for r in range(1, n):
            if(height[r]<lh):
                continue
            rh = height[r]
            bound = min(lh, rh)
            while(l<r):
                space = bound - height[l]
                ans[l] = max(ans[l], space)
                l+=1
            lh = height[l]

        r = n-1
        rh = height[r]
        for l in range(n-1, -1, -1):
            if(height[l]<rh):
                continue
            lh = height[l]
            bound = min(lh, rh)
            while(l<r):
                space = bound - height[r]
                ans[r] = max(ans[r], space)
                r-=1
            rh = height[r]


        return sum(ans)
