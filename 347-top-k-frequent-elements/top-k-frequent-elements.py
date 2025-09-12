class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for e in nums:
            dic[e] = dic.get(e, 0)+1

        dic_ = {}
        mx = 0

        for key, val in dic.items():
            if(val not in dic_):
                dic_[val] = []
            dic_[val].append(key)
            mx = max(mx, val)

        
        ans = []
        for i in range(mx, 0, -1):
            rest = k-len(ans)
            if(i in dic_):
                ans += dic_[i][:rest]
        return ans