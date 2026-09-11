import heapq as hq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []
        max_element = -math.inf

        for i in range(k):
            e = nums[i]
            while(q and q[-1][0]<=e):
                q.pop()
            q.append((e, i))

        ans.append(q[0][0])
        for i in range(k, len(nums)):
            e = nums[i]
            while(q and q[-1][0]<=e):
                q.pop()
            q.append((e, i))

            while(q[0][1]<=(i-k)):
                q.popleft()
            
            ans.append(q[0][0])
        
        return ans