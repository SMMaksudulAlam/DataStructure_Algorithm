class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        mini = min(nums)
        maxi = max(nums)

        if(mini == maxi):
            return 0
        
        def count_moves(mid): #i need to tract the above and below count, instead of above and below distance. Why? We don't want the above distance == below distance, rather we want the increment/decrement count gets lower. So, we should move toward the higher count side while making decision on binary search
            below_count = 0
            above_count = 0
            dis = 0
            for e in nums:
                dis += abs(e - mid)
                if(mid>e):
                    below_count += 1
                else:
                    above_count += 1
            return dis, below_count, above_count

        ans = math.inf

        while(mini<=maxi):
            mid = (mini + maxi)//2 
            dis, below_count, above_count = count_moves(mid)
            ans = min(ans, dis)
            if(above_count > below_count):
                mini = mid+1
            else:
                maxi = mid-1 
        return ans    