class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s = 'X'+s
        ans = [0]*(len(s))
        ans[0] = 1
        
        wordDict = set(wordDict)

        for i in range(1, len(s)):
            for w in wordDict:
                ln = len(w)
                if(i-ln>=0 and ans[i-ln]==1):
                    if(s[i-ln+1:i+1] in wordDict):
                        ans[i] = 1
        return ans[-1]==1