class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        rem = sum(nums)-x
        left = 0
        w = -1
        sm = 0
        right = 0
        while(right<len(nums)):
            sm += nums[right]
            while(sm>rem and left<=right):
                sm-=nums[left]
                left+=1
            if(sm == rem):
                w = max(w, right-left+1)
            right +=1
        return len(nums)-w if w>=0 else -1