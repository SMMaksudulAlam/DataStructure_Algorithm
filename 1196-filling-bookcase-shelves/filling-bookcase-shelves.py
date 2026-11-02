class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        
        dp = {}
        def pack(ind, occupied, max_h):
            if(ind == len(books)):
                return max_h
            
            if((ind, occupied, max_h) in dp):
                return dp[(ind, occupied, max_h)]
            ans_take = math.inf
            ans_not_take = math.inf
            if(occupied + books[ind][0] <= shelfWidth):
                ans_take = pack(ind+1, occupied + books[ind][0], max(max_h, books[ind][1]))
            ans_not_take = max_h + pack(ind+1, books[ind][0], books[ind][1])

            ans = min(ans_take, ans_not_take)
            dp[(ind, occupied, max_h)] = ans
            return ans
        
        ans = pack(0, 0, 0)
        return ans