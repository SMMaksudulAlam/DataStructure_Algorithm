class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPal(s):
            return s == s[::-1]
        dic = {}
        def part(s):
            if(not s):
                return [[]]
            if(s in dic):
                return dic[s]
            ans = []
            for i in range(len(s)):
                if(isPal(s[:i+1])):
                    tempAns = []
                    pre = s[:i+1]
                    postList = part(s[i+1:])
                    for post in postList:
                        tempAns.append([pre]+post)
                    ans+=tempAns
            dic[s] = ans
            return ans
        ans = part(s)
        return ans