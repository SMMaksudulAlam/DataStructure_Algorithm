import heapq as hq
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        ind = len(nums)-2
        while(ind>=0):
            if(nums[ind]<nums[ind+1]):
                break
            ind-=1
        
        if(ind<0):
            left = 0
            right = len(nums)-1
            while(left<=right):
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
            return
        
        ind_right = len(nums)-1
        while(ind_right>ind):
            if(nums[ind_right]>nums[ind]):
                nums[ind_right], nums[ind] = nums[ind], nums[ind_right]
                break
            ind_right-=1
        
        left = ind+1
        right = len(nums)-1
        while(left<=right):
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right-=1
        return
        

