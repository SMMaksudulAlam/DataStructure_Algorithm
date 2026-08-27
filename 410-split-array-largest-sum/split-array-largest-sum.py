class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def count_subarrays(largest_sum):
            count = 1
            sm = 0
            for n in nums:
                if(n>largest_sum):
                    return math.inf
                if(n+sm<=largest_sum):
                    sm += n
                else:
                    count+=1
                    sm = n
            return count

        left = 1
        right = sum(nums)
        ans = 0
        while(left<=right):
            mid = (left+right)//2
            count = count_subarrays(mid)
            if(count<=k):
                ans = mid
                right = mid-1
            else:
                left = mid+1

        count = count_subarrays(ans)
        #print(count, ans)
        if(count <= k and len(nums)>=k):
            return ans
        return -1