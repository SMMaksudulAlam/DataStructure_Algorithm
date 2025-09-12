class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for e in nums:
            if(e in dic):
                return True
            dic[e] = 1
        return False