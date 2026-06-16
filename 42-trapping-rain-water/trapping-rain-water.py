class Solution:
    def trap(self, height: List[int]) -> int:
        ln = len(height)
        ans = [0]*ln

        l = 0
        for r in range(1, ln):
            left_h = height[l]
            right_h = height[r]

            if(left_h > right_h):
                continue
            
            h = min(left_h, right_h)
            while(l<r):
                ans[l] = max(ans[l], h-height[l])
                l+=1
            
        r = ln-1
        for l in range(ln-2, -1, -1):
            left_h = height[l]
            right_h = height[r]

            if(right_h > left_h):
                continue
            
            h = min(left_h, right_h)
            while(l<r):
                ans[r] = max(ans[r], h-height[r])
                r-=1

        #print(ans)
        return sum(ans)
