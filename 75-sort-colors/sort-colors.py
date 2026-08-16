class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        right = len(nums)-1

        cur = 0

        while(cur<=right):
            num  = nums[cur]
            if(num==1):
                cur+=1
            if(num==0):
                if(left==cur):
                    cur+=1
                else:
                    nums[left], nums[cur] = nums[cur], nums[left]
                left+=1
            if(num==2):
                nums[right], nums[cur] = nums[cur], nums[right]
                right-=1
        


            
        