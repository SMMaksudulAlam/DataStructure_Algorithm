import heapq as hq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        ans = []
        for i in range(k):
            hq.heappush(h, (-nums[i], i))
        
        v, ind = h[0]
        ans.append(-v)

        l = 0
        for i in range(k, len(nums)):
            v = nums[i]
            hq.heappush(h, (-v, i))
            l+=1
            while(h and h[0][1]<l):
                hq.heappop(h)

            v, ind = h[0]
            ans.append(-v)
        return ans

