class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sm = 0
        for i in range(k):
            sm += cardPoints[i]
        
        ans = sm
        for i in range(k):
            ind = k-(i+1)
            sm = sm - cardPoints[k-1-i] + cardPoints[-(i+1)]
            ans = max(ans, sm)

        return ans