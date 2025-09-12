class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, e in enumerate(nums):
            rest = target - e
            if(rest in dic):
                return [dic[rest][-1], i]
            if(e not in dic):
                dic[e] = []
            dic[e].append(i)
        return []
        