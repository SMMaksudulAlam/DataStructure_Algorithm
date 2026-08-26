class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = arr
        if(k<arr[0]):
            return k
        
        left = 0
        right = len(nums)-1
        ind = right

        while(left<=right):
            mid = (left+right)//2
            if(nums[mid]-(mid+1)<=k):
                ind = mid
                left = mid+1
            else:
                right = mid-1
        
        remain = k - (nums[ind]-(ind+1))
        #print(ind, nums[ind], remain)
        if(remain==0):
            while(ind>0 and nums[ind]-nums[ind-1] == 1):
                ind-=1
            return nums[ind]-1
        else:
            return nums[ind] + remain
        return -1


