class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        """
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
        """

        #the previous one works, but it is a bit inefficient with TC: O(N*shelfWidth*max_h)

        dp = {}
        def pack(ind):
            if(ind in dp):
                return dp[ind]
            if(ind == len(books)):
                return 0

            ans = math.inf
            h = 0
            occupied = 0
            i = ind
            while(i<len(books) and occupied + books[i][0] <= shelfWidth):
                occupied += books[i][0]
                h = max(h, books[i][1])
                i+=1
                ans = min(ans, h + pack(i))
                
            dp[ind] = ans
            return ans
        
        ans = pack(0)
        return ans