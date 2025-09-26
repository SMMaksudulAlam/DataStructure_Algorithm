class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0
        while(left<len(nums)):
            if(nums[left]==val):
                right = left+1
                while(right<len(nums)):
                    if(nums[right]!=val):
                        nums[left], nums[right] = nums[right], nums[left]
                        break
                    right += 1
                if(right==len(nums)):
                    return left
            left+=1
        return left