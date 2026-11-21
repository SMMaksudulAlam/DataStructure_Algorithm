class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        q = deque()
        length = len(nums)
        left = length - 1
        right = length - 1
        ans = 0
        req_k = 0

        while(left>=0):
            group_count = 1
            num = nums[left]
            
            while(q and q[0][0]<=num):
                req_k += (num - q[0][0])*q[0][1]
                group_count += q[0][1]
                q.popleft()

            q.appendleft([num, group_count])

            while(q and req_k>k):
                req_k -= q[-1][0] - nums[right]
                q[-1][1] -= 1
                right -= 1
                if(q[-1][1] == 0):
                    q.pop()

            ans += (right - left + 1)
            left -= 1

        return ans