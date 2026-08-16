import heapq as hq
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        h = []
        ind = len(nums)-1
        while(ind>=0):
            num = nums[ind]
            hq.heappush(h, -num)

            h_top = -h[0]
            if(h_top>num):
                right_ind = len(nums)-1
                while(h and -h[0]>num):
                    nums[right_ind] = -hq.heappop(h)
                    right_ind-=1
                right_ind+=1
                nums[ind], nums[right_ind] = nums[right_ind], nums[ind]
                ind = right_ind
                break
            ind-=1

        if(ind<0):
            left = 0
            right = len(nums)-1
            while(left<right):
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
            return
        #print(nums)
        while(h):
            nums[ind] = -hq.heappop(h)
            ind-=1
        return
