class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dic = {}
        dic[word1] = []
        dic[word2] = []

        ans = inf
        for i, w in enumerate(wordsDict):
            if(w == word1):
                dic[word1].append(i)
                if(dic[word2]):
                    diff = i - dic[word2][-1]
                    ans = min(ans, diff)
            if(w == word2):
                dic[word2].append(i)
                if(dic[word1]):
                    diff = i - dic[word1][-1]
                    ans = min(ans, diff)
        return ans