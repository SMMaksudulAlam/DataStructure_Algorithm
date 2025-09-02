class Solution:
    def beautySum(self, s: str) -> int:
        count = 0
        ln = len(s)
        for i in range(ln):
            dic = {}
            for j in range(i, ln):
                e = s[j]
                dic[e] = dic.get(e, 0)+1
                keys = dic.values()
                count += max(keys)-min(keys)
        return count