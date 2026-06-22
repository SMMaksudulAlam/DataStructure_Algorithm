import heapq as hq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        h = []
        for i in range(k):
            n = nums[i]
            hq.heappush(h, (-n, i))
        
        ans.append(-h[0][0])
        for i in range(k, len(nums)):
            rmv_ind = i-k
            while(h and h[0][1]<=rmv_ind):
                hq.heappop(h)

            n = nums[i]
            hq.heappush(h, (-n, i))
            ans.append(-h[0][0])
        
        return ans

