class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPal(s):
            return s == s[::-1]

        def part(s):
            if(not s):
                return [[]]
            ans = []
            for i in range(len(s)):
                if(isPal(s[:i+1])):
                    tempAns = []
                    pre = s[:i+1]
                    postList = part(s[i+1:])
                    for post in postList:
                        tempAns.append([pre]+post)
                    ans+=tempAns
            return ans
        ans = part(s)
        return ans