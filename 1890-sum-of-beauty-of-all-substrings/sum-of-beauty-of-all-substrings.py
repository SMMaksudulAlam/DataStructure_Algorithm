class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0
        ln = len(s)
        for i in range(ln):
            dic = {}
            for j in range(i, ln):
                ch = s[j]
                dic[ch] = dic.get(ch, 0)+1
                vals = dic.values()
                ans += (max(vals)-min(vals))
        return ans