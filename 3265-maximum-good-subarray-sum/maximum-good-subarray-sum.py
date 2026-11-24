import heapq as hq
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
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
