import heapq as hq
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        h = []
        ln = len(nums)
        for i in range(ln-1, -1, -1):
            n = nums[i]
            hq.heappush(h, -n)
            if(-h[0] == n):
                continue
            ar = []
            while(h):
                if(-h[0]==n and ar and ar[-1] != n):
                    nums[i] = ar.pop()
                ar.append(-hq.heappop(h))
            j = i+1
            while(ar):
                nums[j] = ar.pop()
                j+=1
            return
        for i in range(ln//2):
            nums[i], nums[ln-1-i] = nums[ln-1-i], nums[i]
        return
        
