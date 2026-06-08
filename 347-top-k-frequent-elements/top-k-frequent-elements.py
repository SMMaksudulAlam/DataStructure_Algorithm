class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for e in nums:
            count[e] = count.get(e, 0)+1

        freq = {}
        max_count = 0
        for key, val in count.items():
            if(val not in freq):
                freq[val] = []
            freq[val].append(key)
            max_count = max(max_count, val)
        
        ans = []
        count_ans = 0
        for i in range(max_count, -1, -1):
            if(i in freq):
                rest = k - count_ans
                if(rest > len(freq[i])):
                    ans += freq[i]
                    count_ans += len(freq[i])
                else:
                    ans += freq[i][:rest]
                    break
        return ans


