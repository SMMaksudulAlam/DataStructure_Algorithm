import heapq as hq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = deque([])
        for i in range(k):
            e = nums[i]
            if(not stack):
                stack.append((e, i))
                continue
            
            while(stack and stack[-1][0]<=e):
                stack.pop()
            
            stack.append((e, i))
        
        ans = []
        ans.append(stack[0][0])
    
        for i in range(k, len(nums)):
            if(stack[0][1]<=(i-k)):
                stack.popleft()
            e = nums[i]
            while(stack and stack[-1][0]<=e):
                stack.pop()
            stack.append((e, i))
            ans.append(stack[0][0])
        return ans


