class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def ispal(s):
            return s == s[::-1]
        def build(s):
            if(not s):
                return [[]]
            ans_comb = []
            for i in range(len(s)):
                if(ispal(s[:i+1])):
                    ans = build(s[i+1:])
                    for a in ans:
                        ans_comb.append([s[:i+1]] + a)
            return ans_comb

            

        ans = build(s)
        return ans