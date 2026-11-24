import heapq as hq
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        dic = {}
        prefix = 0

        for i, e in enumerate(nums):
            prefix += e
            if(e not in dic):
                dic[e] = []
            hq.heappush(dic[e], (-prefix, i))
        
        prefix = 0
        ans = -math.inf
        for i, e in enumerate(nums):
            high = e + k
            low = e - k

            if(high in dic):
                while(dic[high] and dic[high][0][1]<=i):
                    hq.heappop(dic[high])
                if(dic[high]):
                    ahead_prefix, ind = dic[high][0]
                    ahead_prefix = -ahead_prefix
                    ans = max(ans, ahead_prefix - prefix)

            if(low in dic):
                while(dic[low] and dic[low][0][1]<=i):
                    hq.heappop(dic[low])
                if(dic[low]):
                    ahead_prefix, ind = dic[low][0]
                    ahead_prefix = -ahead_prefix
                    ans = max(ans, ahead_prefix - prefix)

            prefix += e
        
        return ans if ans != -math.inf else 0

        #TC --> O(nlogn)
        """
        #my previous approach is looking forward only through max heap. By heap we solve the problem as follows:
        #we want to get the NEXT & HIGHEST prefix sum for the element of high/low
        #here, the heap maintains the NEXT & HIGHEST
        #we get the complexity O(nlogn)

        #However, we can look backward and want the minimum prefix sum for the element of high/low ON THE RUN TIME
        #it does not need the heap to maintain the PREVIOUS & MINIMUM, becuause runtime ensures the PREVIOUS, and we can update the MINIMUM with O(1)
        #thus we can get O(n) TC

        dic = {}
        prefix = 0
        ans = -math.inf

        for i, e in enumerate(nums):
            prefix += e

            high = e + k
            low = e - k

            if(high in dic):
                ans = max(ans, prefix - dic[high] + high)
            if(low in dic):
                ans = max(ans, prefix - dic[low] + low)
            
            if(e not in dic):
                dic[e] = prefix
            else:
                dic[e] = min(dic[e], prefix)

        return ans if ans != -math.inf else 0

        #TC --> O(n)