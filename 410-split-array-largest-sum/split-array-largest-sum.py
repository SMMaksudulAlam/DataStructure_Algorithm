class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def split_count(largest_sum):
            count = 0
            sm = 0
            for n in nums:
                if(n>largest_sum):
                    return inf
                if(sm+n<=largest_sum):
                    sm += n
                else:
                    count+=1
                    sm = n
            return count+1
        
        left = min(nums)
        right = sum(nums)

        while(left <= right):
            if(left == right):
                return left
            if(left+1==right):
                if(split_count(left)<=k):
                    return left
                return right

            mid = (left+right)//2
            if(split_count(mid)<=k):
                right = mid
            else:
                left = mid
        return -1