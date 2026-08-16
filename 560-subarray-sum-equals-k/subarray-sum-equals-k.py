class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}

        tot_sum = 0
        ans = 0
        for n in nums:
            tot_sum += n
            diff = tot_sum - k
            if(diff in prefix):
                ans += prefix[diff]
            prefix[tot_sum] = prefix.get(tot_sum, 0) + 1
        return ans